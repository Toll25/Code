import Board from './Board.jsx'
import {useState} from "react";
import {
    Button, Modal,
    ModalBody,
    ModalContent,
    ModalFooter,
    ModalHeader,
    Slider,
    useDisclosure,
} from "@nextui-org/react";

function App() {
    const [sizeX, setSizeX] = useState(10)
    const [sizeY, setSizeY] = useState(10)
    const [numberOfMines, setNumberOfMines] = useState(10)
    const [triggerRerender, setTriggerRerender] = useState(false)
    const {isOpen: isOpenWin, onOpen: onOpenWin, onOpenChange: onOpenChangeWin} = useDisclosure();
    const {isOpen: isOpenLose, onOpen: onOpenLose, onOpenChange: onOpenChangeLose} = useDisclosure();


    let maxNumberOfMines = sizeX * sizeY;

    function lose() {
        onOpenLose()
    }

    function win() {
        onOpenWin()
    }

    return (
        <>
            <Modal isOpen={isOpenWin} onOpenChange={onOpenChangeWin} className="dark">
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader className="flex flex-col gap-1">You Win!</ModalHeader>
                            <ModalBody>
                                <p>
                                    You have won the game!
                                </p>
                            </ModalBody>
                            <ModalFooter>
                                <Button color="primary" onPress={onClose}>
                                    Yayyy
                                </Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
            <Modal isOpen={isOpenLose} onOpenChange={onOpenChangeLose} className="dark">
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader className="flex flex-col gap-1">You Lose!</ModalHeader>
                            <ModalBody>
                                <p>
                                    You have lost the game!
                                </p>
                            </ModalBody>
                            <ModalFooter>
                                <Button color="primary" onPress={onClose}>
                                    :(
                                </Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>

            <div className="p-3 inline-block w-full">
                <div>
                    <Slider
                        size="lg"
                        step={1}
                        color="foreground"
                        label="X Size"
                        showSteps={true}
                        maxValue={24}
                        minValue={5}
                        defaultValue={10}
                        value={sizeX}
                        onChange={setSizeX}
                        className="max-w-md inline-block p-3"
                    />
                    <Slider
                        size="lg"
                        step={1}
                        color="foreground"
                        label="Y Size"
                        showSteps={true}
                        maxValue={24}
                        minValue={5}
                        defaultValue={10}
                        value={sizeY}
                        onChange={setSizeY}
                        className="max-w-md inline-block p-3"
                    />
                    <Slider
                        size="lg"
                        step={1}
                        color="foreground"
                        label="Mines"
                        marks={[
                            {
                                value: maxNumberOfMines * 0.2,
                                label: "20%",
                            },
                            {
                                value: maxNumberOfMines * 0.5,
                                label: "50%",
                            },
                            {
                                value: maxNumberOfMines * 0.8,
                                label: "80%",
                            },
                        ]}
                        maxValue={sizeX * sizeY}
                        minValue={1}
                        defaultValue={10}
                        value={numberOfMines}
                        getValue={(mines) => `${mines} of ${maxNumberOfMines} Mines (${((mines / maxNumberOfMines) * 100).toFixed(2)}%)`}
                        onChange={setNumberOfMines}
                        className="max-w-md inline-block p-3"
                    />
                    <Button color="primary" className="relative top-[50%] -translate-y-1/2" onClick={setTriggerRerender}>
                        New Game
                    </Button>
                </div>

                <Board size1={sizeX} size2={sizeY} numberOfMines={numberOfMines} clickTrigger={triggerRerender}
                       loseTrigger={lose} winTrigger={win}></Board>
            </div>
        </>
    )
}

export default App
