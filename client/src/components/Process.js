import runProcess from '../models/process';

const Process = ({session_id}) => {
    return (
        <div className="container">
            <div className="columns is-centered">
                <p>
                    <button id="process-btn" className="button is-primary" onClick={runProcess}>
                        Process my videos
                    </button>
                </p>
                <p id="process-response"></p>
            </div>
        </div>
    )
}
export default Process;