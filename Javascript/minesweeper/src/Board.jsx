import { useState, useEffect } from 'react';

const MineBoard = ({ size }) => {
    const [grid, setGrid] = useState([]);
    const [isGameOver, setGameOver] = useState(false);
    const [isGameWon, setGameWon] = useState(false);
    const [clickTrigger, setClickTrigger] = useState(false);

    useEffect(() => {
        const generateGrid = () => {
            const newGrid = Array.from({ length: size }, () =>
                Array.from({ length: size }, () => ({
                    isMine: Math.random() < 0.2,
                    isFlagged: false,
                    isOpen: false,
                    value: 0,
                }))
            );
            setGrid(newGrid);
            setGameOver(false);
            setGameWon(false);
        };

        generateGrid();
    }, [ size]);

    const handleCellClick = (row, col) => {
        if (isGameOver || isGameWon) return;

        setGrid((prevGrid) => {
            const newGrid = [...prevGrid];
            const currentCell = newGrid[row][col];

            if (currentCell.isFlagged || currentCell.isOpen) {
                return newGrid;
            }

            if (currentCell.isMine) {
                currentCell.value = "M";
                setGameOver(true);
            } else {
                openCell(newGrid, row, col);
                checkGameStatus(newGrid);
            }


            return newGrid;
        });
        setClickTrigger(!clickTrigger);
    };

    const handleRightClick = (event, row, col) => {
        event.preventDefault();

        if (isGameOver || isGameWon) return;

        setGrid((prevGrid) => {
            const newGrid = [...prevGrid];
            const currentCell = newGrid[row][col];

            if (!currentCell.isOpen) {
                console.log("Before toggle:", newGrid[row][col].isFlagged);

                if(newGrid[row][col].isFlagged === true) {
                    newGrid[row][col].isFlagged = false;
                } else {
                    newGrid[row][col].isFlagged = true;
                    console.log("Set to true")
                }


                console.log("After toggle:", newGrid[row][col].isFlagged);
            }

            checkGameStatus(newGrid);

            console.log(newGrid)
            return newGrid;
        });
        setClickTrigger(!clickTrigger);
    };

    const openCell = (grid, row, col) => {
        if (
            row < 0 ||
            row >= size ||
            col < 0 ||
            col >= size ||
            grid[row][col].isOpen ||
            grid[row][col].isFlagged
        ) {
            return;
        }

        grid[row][col].isOpen = true;

        if (!grid[row][col].isMine) {
            let minesAround = 0;

            for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    const newRow = row + i;
                    const newCol = col + j;

                    if (newRow >= 0 && newRow < size && newCol >= 0 && newCol < size) {
                        minesAround += grid[newRow][newCol].isMine ? 1 : 0;
                    }
                }
            }

            grid[row][col].value = minesAround;

            if (minesAround === 0) {
                for (let i = -1; i <= 1; i++) {
                    for (let j = -1; j <= 1; j++) {
                        openCell(grid, row + i, col + j);
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
            console.log("Game won")
            setGameWon(true);
            setGameOver(true);
        }
    };

    return (
        <div
            className={`minesweeper ${isGameOver ? 'game-over' : ''} ${
                isGameWon ? 'game-won' : ''
            }`}
        >
            {grid.map((row, rowIndex) => (
                <div key={rowIndex} className="row">
                    {row.map((cell, colIndex) => (
                        <BoardCell
                            key={`${rowIndex}-${colIndex}`}
                            isMine={cell.isMine}
                            isFlagged={cell.isFlagged}
                            isOpen={cell.isOpen}
                            value={cell.value}
                            onClick={() => handleCellClick(rowIndex, colIndex)}
                            onRightClick={(event) =>
                                handleRightClick(event, rowIndex, colIndex)
                            }
                        />
                    ))}
                </div>
            ))}
        </div>
    );
};

const BoardCell = ({ onClick, onRightClick, isMine, isFlagged, isOpen, value }) => {

    return (
        <div
            className={`cell ${isFlagged ? 'flagged' : ''} ${isOpen ? 'open' : ''}`}
            onClick={onClick}
            onContextMenu={onRightClick}
        >
            {isOpen ? (isMine ? 'M' : value) : isFlagged ? 'F' : ''}
        </div>
    );
};

export default MineBoard;
