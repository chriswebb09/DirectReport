'use strict';
const elem = React.createElement;
const { useState, useEffect } = React;


const rootElement = document.getElementById('root')

class ReportItem extends React.Component {
    render() {
        return (
            <div className="mx-50 content-center mt-20 my-28 h-150">
                <div className="flex flex-col justify-center my-6 mx-60">
                    <h1 className="self-center text-3xl text-gray-700 text-center font-bold">Report</h1>
                    <p>{this.props.report["raw_input"]}</p>
                </div>
            </div>
        );
    }
}
const App = () => {
    const [reportData, setReportData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/getlist`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((actualData) => {
                setReportData(actualData[0]);
                setError(null);
            })
            .catch((err) => {
                setError(err.message);
                setReportData(null)
            })
            .finally(() => {
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div>{`There is a problem fetching the post data - ${error}`}</div>
        )
    } else {
        if (reportData != null) {
            return (
                <div><ReportItem name="Report" report={reportData}/></div>
            )
        } else {
            return (
                <div>
                    {/*<EmptyEntryList/>*/}
                </div>
            )
        }
    }
}

const domContainer = document.querySelector("#root");
ReactDOM.render(<App/>, domContainer);
