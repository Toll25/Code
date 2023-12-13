import {getAllExoplanets} from "../models/exoplanetsModel.js";

const exoplanetsService = {
    getExoplanets() {
        return getAllExoplanets();
    }
};

export default exoplanetsService;