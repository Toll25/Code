import { useState, useEffect } from 'react';
import {FaBomb, FaFlag} from "react-icons/fa";

const MineBoard = ({ size1, size2, numberOfMines, clickTrigger, winTrigger, loseTrigger}) => {
    const [grid, setGrid] = useState([]);
    const [isGameOver, setGameOver] = useState(false);
    const [isGameWon, setGameWon] = useState(false);

    useEffect(() => {

        const generateGrid= () => {
            const newGrid = Array.from({length: size1}, () =>
                Array.from({length: size2}, () => ({
                    isMine: false,
                    isFlagged: false,
                    isOpen: false,
                    value: 0,
                }))
            );

            let newNumberOfMines=numberOfMines
            if(newNumberOfMines>(size1*size2)){
                newNumberOfMines=size1*size2
            }

            for (let i = 0; i < newNumberOfMines; i++) {
                let coordX = Math.floor(Math.random() * size1)
                let coordY = Math.floor(Math.random() * size2)
                do {
                    coordX = Math.floor(Math.random() * size1)
                    coordY = Math.floor(Math.random() * size2)
                } while (newGrid[coordX][coordY].isMine)
                for (let x = -1; x<=1;x++){
                    for (let y = -1; y<=1;y++){
                        if(x===0 && y===0){
                            newGrid[coordX][coordY].value=-1
                            newGrid[coordX][coordY].isMine=true
                        }else{
                            if (coordX + x >= 0 && coordX + x < size1 && coordY + y >= 0 && coordY + y < size2) {
                                newGrid[coordX + x][coordY + y].value += 1;
                            }
                        }
                    }
                }
            }
            setGrid(newGrid);
            setGameOver(false);
            setGameWon(false);
        }
        generateGrid();
    }, [size1,size2,numberOfMines,clickTrigger]);

    const handleCellClick = (row, col) => {
        if (isGameOver || isGameWon) return;

        setGrid((prevGrid) => {
            const newGrid = [...prevGrid];
            const currentCell = newGrid[row][col];

            if (currentCell.isFlagged || currentCell.isOpen) {
                return newGrid;
            }

            if (currentCell.isMine) {
                openAll();
                loseTrigger()
                setGameOver(true);
            } else {
                openCell(newGrid, row, col);
                checkGameStatus(newGrid);
            }


            return newGrid;
        });
    };

    const handleRightClick = (event, row, col) => {
        event.preventDefault();

        if (isGameOver || isGameWon) return;

        const newGrid = [...grid];
        const currentCell = newGrid[row][col];

        if (!currentCell.isOpen) {

            newGrid[row][col].isFlagged = !newGrid[row][col].isFlagged;
        }

        checkGameStatus(newGrid);

        setGrid(newGrid);
    };

    const openAll = () => {
        for(let i = 0; i<size1; i++){
            for (let j=0; j<size2;j++){
                grid[i][j].isOpen=true;
            }
        }
    }

    const openCell = (grid, row, col) => {
        if (
            row < 0 ||
            row >= size1 ||
            col < 0 ||
            col >= size2 ||
            grid[row][col].isOpen ||
            grid[row][col].isFlagged
        ) {
            return;
        }

        grid[row][col].isOpen = true;

        if (!grid[row][col].isMine) {
            if (grid[row][col].value === 0) {
                for (let i = -1; i <= 1; i++) {
                    for (let j = -1; j <= 1; j++) {
                        const newRow = row + i;
                        const newCol = col + j;
                        if (newRow >= 0 && newRow < size1 && newCol >= 0 && newCol < size2) {
                            openCell(grid, newRow, newCol);
                        }
                    }
                }
            }
        }
    };

    const checkGameStatus = (grid) => {
        const isGameWon =
            grid.every((row) =>
                row.every((cell) => (cell.isMine ? cell.isFlagged : cell.isOpen))
            ) ||
            grid.some((row) => row.some((cell) => cell.isMine && cell.isOpen));

        if (isGameWon) {
            winTrigger()
            setGameWon(true);
        }
    };

    return (
        <div
            className={`minesweeper ${
                isGameWon || isGameOver ? 'noInteract' : ''
            } w-fit`}
            style={{ gridTemplateColumns: `repeat(${size2}, 1fr)` }}
        >
            {grid.map((row, rowIndex) =>
                row.map((cell, colIndex) => (
                    <BoardCell
                        key={`${rowIndex}-${colIndex}`}
                        isMine={cell.isMine}
                        isFlagged={cell.isFlagged}
                        isOpen={cell.isOpen}
                        value={cell.value}
                        onClick={() => handleCellClick(rowIndex, colIndex)}
                        onRightClick={(event) => handleRightClick(event, rowIndex, colIndex)}
                    />
                ))
            )}
        </div>
    );
};

const BoardCell = ({ onClick, onRightClick, isMine, isFlagged, isOpen, value }) => {

    return (
        <div
            className={`cell ${isFlagged ? 'flagged' : ''} ${isOpen ? 'open' : ''} flex justify-center items-center`}
            onClick={onClick}
            onContextMenu={onRightClick}
        >
            {isOpen ? (isMine ? <div><FaBomb /></div> : (value === 0 ? null : value)) : isFlagged ? <div><FaFlag /></div> : ''}
        </div>
    );
};

export default MineBoard;
