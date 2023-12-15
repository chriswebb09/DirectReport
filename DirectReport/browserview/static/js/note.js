'use strict';
const { useState, useEffect } = React;

function jsonEscape(str)  {
    return str.replace(/\n/g, "\\\\n").replace(/\r/g, "\\\\r").replace(/\t/g, "\\\\t");
}
class ReportItem extends React.Component {
    render() {
        console.log(this.props.report["summary"])
        console.log(this.props.report["areas_of_focus"])
        console.log(this.props.report["total_commits"])
        console.log(this.props.report["conclusion"])
        console.log(this.props.report["highlights"])

        return (
            <div className="mx-50 content-center mt-20 my-28 h-150">
                <div className="flex flex-col justify-center my-6 mx-60">
                    <h1 className="self-center text-3xl text-gray-700 text-center font-bold">Report</h1>
                    {this.props.report !== undefined ?
                        <div className="px-2 mb-1 text-xs text-blue-700">{this.props.report["summary"]}</div> : null
                    }
                    {this.props.report !== undefined ?
                        <div className="px-2 mb-1 text-xs text-blue-700">{this.props.report["conclusion"]}</div> : null
                    }
                    {this.props.report["highlights"] && this.props.report["highlights"].map(report =>
                            <div className="flex flex-col justify-center my-6 mx-60">
                                <h1 className="self-center text-3xl text-gray-700 text-center font-bold">{report["title"]}</h1>
                                <div className="px-2 mb-1 text-xs text-blue-700">{report["description"]}</div>
                            </div>
                    )}
                </div>
            </div>
        );
    }
}

const App = () => {

    const [reportData, setReportData] = useState(null);
    const [teamData, setTeamData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        var idElement = window.location.pathname.split("/").pop();
        fetch('/getreport/' + idElement)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((actualData) => {
                console.log(actualData["report"].team);
                setReportData(actualData["report"].report);
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
                <div>
                    <ReportItem name="Report" report={reportData} team={teamData}/>
                </div>
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
