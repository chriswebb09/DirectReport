const { useState, useEffect } = React;

class EntryList extends React.Component {
    render() {
        return (
            <div class="grid grid-cols-3 gap-1 mb-20 mx-10">
                {this.props.listdata.map(item =>
                    <div class="col-span-1 justify-center my-5">
                        <article className="mx-8 mt-8 w-90 rounded-2xl border border-gray-200 p-1 shadow-lg transition hover:shadow-xl">
                            <a className="block rounded-xl bg-white p-1 sm:p-6 lg:p-8" href={'/entry/' + item.uuid}>
                                <div className="mt-1">
                                    <h2 className="text-2xl font-bold text-gray-800 sm:text-xl">{'Topic: ' + item.user_id}</h2>
                                    <p className="mt-3 text-sm text-justify line-clamp-5 text-gray-500">{'Entry: ' + item.raw_input}</p>
                                </div>
                            </a>
                        </article>
                    </div>
                )}
            </div>
        );
    }
}

class EmptyEntryList extends React.Component {
    render() {
        return (
            <div className="mx-50 content-center mt-20 my-28 h-150">
                <div className="flex flex-col justify-center my-6 mx-60">
                    <h1 className="self-center text-3xl text-gray-700 text-center font-bold">Add New Entry</h1>
                    <EntryForm/>
                </div>
            </div>
        );
    }
}


const App = () => {
    const [listData, setListData] = useState([]);
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
                setListData(actualData);
                setError(null);
            })
            .catch((err) => {
                setError(err.message);
                setListData(null)
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
        if (listData.length > 0) {
            return (
                <div><EntryList name="Entry List" listdata={listData}/></div>
            )
        } else {
            return (
                <div>
                    <EmptyEntryList/>
                </div>
            )
        }
    }
}

const domContainer = document.querySelector("#root");
ReactDOM.render(<App/>, domContainer);
