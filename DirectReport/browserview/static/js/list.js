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
                                    <h2 className="text-2xl font-bold text-gray-800 sm:text-xl">{'Topic: ' + item.topic}</h2>
                                    <p className="mt-3 text-sm text-justify line-clamp-5 text-gray-500">{'Entry: ' + item.message}</p>
                                </div>
                            </a>
                        </article>
                    </div>
                )}
            </div>
        );
    }
}

class EntryForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            topic: '',
            entry: ''
        };
        this.handleTopicChange = this.handleTopicChange.bind(this);
        this.handleEntryChange = this.handleEntryChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleTopicChange(event) {
        this.setState({topic: event.target.value});
    }

    handleEntryChange(event) {
        this.setState({entry: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.topic + ' entry: ' + this.state.entry);
        event.preventDefault();
        axios({
            method: 'post',
            url: "http://127.0.0.1:5000/list",
            headers: {'content-type': 'application/json'},
            data: {"topic": this.state.topic, "entry": this.state.entry}
        }).then(result => {
            console.log(result.data);
        }).catch(error => {
            console.log(error);
        })
    }

    render() {
        return (
            <form className="w-3/4 py-2 px-2 self-center" onSubmit={this.handleSubmit}>
                <div class="items-center mb-6">
                    <div className="flex my-10 mr-40">
                        <div class="w-1/6">
                            <label className="text-2xl text-gray-700 font-medium text-right mb-1 mb-0 pr-2">Topic:</label>
                        </div>
                        <div class="w-5/6">
                            <input className="rounded w-full" type="text" value={this.state.topic}  onChange={this.handleTopicChange}/>
                        </div>
                    </div>
                    <div className="flex my-6 mr-40">
                        <div class="w-1/6">
                            <label className="text-2xl text-gray-700 font-medium text-right mb-1 mb-0 pr-2">Entry:</label>
                        </div>
                        <div class="w-5/6">
                            <textarea cols="70" rows="10"  className="text-base text-gray-700 placeholder-gray-600 border rounded-lg focus:shadow-outline" value={this.state.entry} onChange={this.handleEntryChange}></textarea>
                        </div>
                    </div>
                    <div className="flex justify-center my-6">
                        <button className="self-center bg-blue-500 hover:bg-gray-400 text-white text-xl font-semibold py-4 px-6 rounded-lg" type="submit">Create Account</button>
                    </div>
                </div>
            </form>
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
                setListData(actualData)
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
