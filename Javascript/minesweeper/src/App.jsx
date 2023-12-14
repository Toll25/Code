import './App.css'
import Board from './Board.jsx'
import {useId, useState} from "react";

function App() {
    const [boardSize, setBoardSize] = useState(4); // Initial board size
    const sizeId = useId();

    const handleSizeChange = (event) => {
           // const newSize = parseInt(event.target.value, 8);
            setBoardSize(8);
    };

  return (
      <>
          <label htmlFor={sizeId}>Board Size:</label>
          <input
              id={sizeId}
              name="size"
              type="number"
              value={boardSize}
              onChange={handleSizeChange}
              placeholder={"value above 2"}
              min={2}
          />
          <Board size={boardSize}></Board>
      </>
  )
}

export default App
