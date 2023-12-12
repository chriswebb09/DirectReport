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
        // console.log(this.props.team)
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
                // console.log(actualData);
                // console.log(typeof actualData["report"])
                // var newData = {
                //     "team": [
                //         {
                //             "name":"Adrian Prantl",
                //             "accomplishments":"Adrian made significant contributions to the DebugInfo and SILGen, including adding support for debug info for coroutine alloc as,inlined and specialized generic variables.He also worked on the mangling testcase,fixed source locations of variable assignments and function calls, and added build-script support for SwiftLLDB backwards-compatibility tests.",
                //             "commits":"67"
                //         },
                //         {
                //             "name":"Alan Zeino",
                //             "accomplishments":"Alan fixed a typo in the code example in libSyntax README.",
                //             "commits":"1"
                //         },
                //         {
                //             "name":"Alejandro",
                //             "accomplishments":"Alejandro removed awarning, made some documentation fixes, fixed Binary Floating Point. random(in:) open range returning upperBound, and fixed a minor code typo in SILPro.",
                //             "commits":"3"
                //         },
                //         {
                //             "name":"Akshay Shrimali",
                //             "accomplishments":"Akshay updated the README.md file.",
                //             "commits":"1"
                //         },
                //         {
                //             "name":"Ahmad Alhashemi",
                //             "accomplishments":"Ahmad worked on the Parser, detecting non breaking space U+00A0 and providing a fix.He also made minor style edits and added more non-breaking space testcases.",
                //             "commits":"5"
                //         },
                //         {
                //             "name":"Albin Sadowski",
                //             "accomplishments":"Albin fixed syntax highlighting in CHANGELOG.",
                //             "commits":"1"
                //         },
                //         {
                //             "name":"Alex Blewitt",
                //             "accomplishments":"Alex worked on several fixes including compare for lhs and rhs, using || instead of && for kind comparison,removing duplicate conditional check and duplicate if statement.",
                //             "commits":"5"
                //         }
                //     ],
                //     "report":{
                //         "summary":"The team made significant progress this week with a total of 83 commits.The main focus was on DebugInfo and SILGen enhancements, Parser improvements, and various fixes.",
                //         "total_commits":"83",
                //         "areas_of_focus":[
                //             "DebugInfo and SILGen Enhancements",
                //             "Parser Improvements",
                //             "Various Fixes"
                //         ],
                //         "highlights":[
                //             {
                //                 "title":"DebugInfo and SILGen Enhancements",
                //                 "description":"Adrian Prantl made significant contributions to the DebugInfo and SILGen, including adding support for debuginfo for coroutine allocas, inlined and specialized generic variables."
                //             },
                //             {
                //                 "title":"Parser Improvements",
                //                 "description":"Ahmad Alhashemi worked on the Parser,detecting non breaking space U+00A0 and providing a fix."
                //             },
                //             {
                //                 "title":"Various Fixes",
                //                 "description":"The team worked on several fixes including compare for lhs and rhs, using || instead of && for kind comparison,removing duplicate conditional check and duplicate if statement."
                //             }
                //         ],
                //         "conclusion":"The team demonstrated good progress this week, with a focus on enhancing DebugInfo and SILGen, improving the Parser, and implementing various fixes. The team should continue to focus on these areas in the coming week."
                //     },
                //     "broad_categories":{
                //         "debug_info":16,
                //         "code_maintenance":9,
                //         "documentation":7,
                //         "test_related":6,
                //         "nonbreaking_space_handling":5,
                //         "readme_update":1,
                //         "syntax_fix":1
                //     },
                //     "shortlog":{
                //         "Adrian Prantl":67,
                //         "Ahmad Alhashemi":5,
                //         "Akshay Shrimali":1,
                //         "Alan Zeino":1,
                //         "Albin Sadowski":1,
                //         "Alejandro":3,
                //         "Alex Blewitt":5
                //     }
                // // }
                // // var actualJSON = JSON.stringify(actualData);
                // // console.log(JSON.parse(actualJSON));
                // // var escaped = jsonEscape(actualJSON);
                // // console.log(escaped)
                // // var dataEscape = JSON.parse(escaped);
                // // console.log(dataEscape);
                // // console.log(jsonEscape(dataEscape["report"]))
                // // var dataEscape2 = JSON.stringify(jsonEscape(dataEscape["report"]));
                // // console.log(dataEscape2)
                // setReportData(JSON.parse(actualJSON));
                // // setReportData(newData["team"]);
                // const parsedStr = JSON.parse(JSON.stringify(actualData["report"]));
                // console.log(parsedStr);
                // console.log(typeof parsedStr)
                // var goodQuotes = parsedStr.replaceAll(/[\u2018\u2019]/g, "'").replaceAll(/[\u201C\u201D]/g, '"');
                // console.log(goodQuotes);
                // const parsedStr2 = JSON.parse(goodQuotes);
                // console.log(parsedStr2);
                // console.log(typeof parsedStr2)
                // console.log(window.location.pathname.split("/").pop());
                // var stringed = JSON.stringify(actualData[0]["report"].toString())
                // var parsedStr = JSON.parse(stringed);
                // console.log(JSON.stringify(parsedStr["team"]))
                // stringed = stringed.replace(/"/g, "'");
                // stringed = stringed.replace(/'/g, '"');
                //  console.log(stringed)
                //stringed.replaceAll("\'", "\"");
                // console.log(JSON.parse(stringed))
                // setReportData(actualData[0]["report"]);
                console.log(actualData["report"].team);
                // console.log(JSON.parse(actualData["report"]))
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
