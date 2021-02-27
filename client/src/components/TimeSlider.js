import Nouislider from "nouislider-react";
import "nouislider/distribute/nouislider.css";


const TimeSlider = () => {
    return (
        <div className="columns is-vcentered">
            <div className="column is-narrow has-text-centered">00:00</div>
            <div className="column">
                <Nouislider range={{ min: 0, max: 100 }} start={[0, 100]} connect />
            </div>
            <div className="column is-narrow has-text-centered">01:32</div>
        </div>
    );
}


export default TimeSlider;