import {Chat} from "../components/Chat/Chat";
import {CarForm} from "../components/CarContainer/CarForm";
import {Cars} from "../components/CarContainer/Cars";

const CarPage = () => {
    return (
        <div>
            <CarForm/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {CarPage};