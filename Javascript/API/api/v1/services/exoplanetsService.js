import {exoplanetsModel} from "../models/exoplanetsModel.js";

const exoplanetsService = {
    getExoplanets() {
        return exoplanetsModel;
    }
};

export default exoplanetsService;