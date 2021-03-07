import { useState } from 'react';
import Nouislider from "nouislider-react";
import "nouislider/distribute/nouislider.css";


const TimeSlider = ({start_at, end_at, duration, setStartAt, setEndAt, autoSave}) => {
    
    const updateTimes = (values) => {
        setStartAt(Number(values[0]));
        setEndAt(Number(values[1]));
        autoSave();
    }

   const toTimeString = (timeInt) => {
        let hours = ('0000'+Math.floor(timeInt/60)).slice(-2);
        let minutes = ('0000'+Math.floor(timeInt%60)).slice(-2);
        return `${hours}:${minutes}`
    }

    return (
        <div className="columns is-vcentered">
            <div className="column is-narrow has-text-centered">{toTimeString(start_at)}</div>
            <div className="column">
                <Nouislider 
                    range={{ min: 0, max: Math.floor(duration) }}
                    step={1}
                    start={[start_at, end_at]} 
                    onChange={updateTimes}
                    connect 
                />
            </div>
            <div className="column is-narrow has-text-centered">{toTimeString(end_at)}</div>
        </div>
    );
}

export default TimeSlider;