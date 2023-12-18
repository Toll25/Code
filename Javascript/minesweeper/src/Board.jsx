import {useState, useEffect, useCallback} from 'react';
import {FaBomb, FaFlag} from "react-icons/fa";

const MineBoard = ({size1: sizeX, size2: sizeY, numberOfMines, clickTrigger, winTrigger, loseTrigger}) => {
    const [grid, setGrid] = useState([]);
    const [isGameOver, setGameOver] = useState(false);
    const [isGameWon, setGameWon] = useState(false);

    const generateGrid = () => {
        const newGrid = Array.from({length: sizeX}, () =>
            Array.from({length: sizeY}, () => ({
                isMine: false,
                isFlagged: false,
                isOpen: false,
                value: 0,
            }))
        );

        let newNumberOfMines = numberOfMines
        if (newNumberOfMines > (sizeX * sizeY)) {
            newNumberOfMines = sizeX * sizeY
        }

        for (let i = 0; i < newNumberOfMines; i++) {
            let coordX = Math.floor(Math.random() * sizeX)
            let coordY = Math.floor(Math.random() * sizeY)
            do {
                coordX = Math.floor(Math.random() * sizeX)
                coordY = Math.floor(Math.random() * sizeY)
            } while (newGrid[coordX][coordY].isMine)
            for (let x = -1; x <= 1; x++) {
                for (let y = -1; y <= 1; y++) {
                    if (x === 0 && y === 0) {
                        newGrid[coordX][coordY].value = -1
                        newGrid[coordX][coordY].isMine = true
                    } else {
                        if (coordX + x >= 0 && coordX + x < sizeX && coordY + y >= 0 && coordY + y < sizeY) {
                            newGrid[coordX + x][coordY + y].value += 1;
                        }
                    }
                }
            }
        }
        setGrid(newGrid);
        setGameOver(false);
        setGameWon(false);
    };

    useEffect(() => {
        generateGrid()
    }, [sizeX, sizeY, numberOfMines, clickTrigger]);

    useEffect(() => {
        if (isGameOver) {
            loseTrigger();
        }
        if (isGameWon) {
            winTrigger();
        }
    }, [isGameOver, isGameWon]);

    const handleCellClick = useCallback((row, col) => {
        if (isGameOver || isGameWon) return;

        setGrid((prevGrid) => {
            const newGrid = [...prevGrid];
            const currentCell = newGrid[row][col];

            if (currentCell.isFlagged || currentCell.isOpen) {
                return newGrid;
            }

            if (currentCell.isMine) {
                openAll();
                setGameOver(true);
            } else {
                openCell(newGrid, row, col);
                checkGameStatus(newGrid);
            }

            return newGrid;
        });
    }, [isGameOver, isGameWon, grid]);


    const handleRightClick = useCallback((event, row, col) => {
        event.preventDefault();

        if (isGameOver || isGameWon) return;

        const newGrid = [...grid];
        const currentCell = newGrid[row][col];

        if (!currentCell.isOpen) {
            newGrid[row][col].isFlagged = !newGrid[row][col].isFlagged;
        }

        checkGameStatus(newGrid);

        setGrid(newGrid);
    }, [isGameOver, isGameWon, grid]);

    const openAll = () => {
        grid.forEach((row) => {
            row.forEach((cell) => {
                cell.isOpen = true
            })
        })
    }

    const openCell = (grid, row, col) => {
        if (
            row < 0 ||
            row >= sizeX ||
            col < 0 ||
            col >= sizeY ||
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
                        if (newRow >= 0 && newRow < sizeX && newCol >= 0 && newCol < sizeY) {
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

    const calculateCorners = (row, col) => {
        if (row === undefined || col === undefined) {
            return ""
        }
        let cell = grid[row][col]
        let roundedCorners = "";

        function checkCell(x, y) {
            if (x < 0 || x >= sizeX) {
                return true
            }
            if (y < 0 || y >= sizeY) {
                return true
            }
            if (grid[x] !== undefined && grid[x][y] !== undefined) {
                return grid[x][y].isOpen
            }
            return false
        }

        if (!cell.isOpen) {
            if (checkCell(row - 1, col) && checkCell(row, col - 1)) {
                roundedCorners += "rounded-tl ";
            }
            if (checkCell(row - 1, col) && checkCell(row, col + 1)) {
                roundedCorners += "rounded-tr ";
            }
            if (checkCell(row + 1, col) && checkCell(row, col - 1)) {
                roundedCorners += "rounded-bl ";
            }
            if (checkCell(row + 1, col) && checkCell(row, col + 1)) {
                roundedCorners += "rounded-br ";
            }
        }

        if (cell.isOpen) {
            if (!checkCell(row - 1, col) && !checkCell(row, col - 1)) {
                roundedCorners += "rounded-tl ";
            }
            if (!checkCell(row - 1, col) && !checkCell(row, col + 1)) {
                roundedCorners += "rounded-tr ";
            }
            if (!checkCell(row + 1, col) && !checkCell(row, col - 1)) {
                roundedCorners += "rounded-bl ";
            }
            if (!checkCell(row + 1, col) && !checkCell(row, col + 1)) {
                roundedCorners += "rounded-br ";
            }
        }

        return roundedCorners;
    };


    return (
        <div
            className={`minesweeper ${
                isGameWon || isGameOver ? 'noInteract' : ''
            } w-fit`}
            style={{gridTemplateColumns: `repeat(${sizeY}, 1fr)`}}
        >
            {grid.map((row, rowIndex) =>
                row.map((cell, colIndex) => (
                    <BoardCell
                        key={`${rowIndex}-${colIndex}`}
                        cell={cell}
                        onClick={() => handleCellClick(rowIndex, colIndex)}
                        onRightClick={(event) => handleRightClick(event, rowIndex, colIndex)}
                        roundedCorners={calculateCorners(rowIndex, colIndex)}
                    />
                ))
            )}
        </div>
    );
};

const BoardCell = ({onClick, onRightClick, cell, roundedCorners}) => {

    return (
        <div
            className={`cell ${cell.isFlagged ? 'flagged' : ''} ${cell.isOpen ? 'open' : ''} flex justify-center items-center ${roundedCorners} `}
            onClick={onClick}
            onContextMenu={onRightClick}
        >
            {
                cell.isOpen
                    ? cell.isMine
                        ? <div><FaBomb/></div>
                        : (
                            cell.value === 0
                                ? null
                                : cell.value
                        )
                    : cell.isFlagged
                        ? <div><FaFlag/></div>
                        : ''
            }
        </div>
    );
};

export default MineBoard;
