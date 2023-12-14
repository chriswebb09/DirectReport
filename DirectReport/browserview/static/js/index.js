'use strict';
const elem = React.createElement;

class Home extends React.Component {
    render() {
        return elem(
            'div',
            null,
            React.createElement(
                'div',
                {
                    className: "py-20 flex h-50",
                    style: {background: "linear-gradient(90deg, #667eea 0%, #764ba2 100%)"}
                },
                React.createElement(
                    "div",
                    {
                        className: "container mx-auto px-6"
                    },
                    React.createElement(
                        "h2",
                        {
                            className: "my-1 text-3xl font-bold mb-5 text-white"
                        },
                        "DirectReport."
                    ),
                    React.createElement(
                        "h3",
                        {
                            className: "my-1 text-lg mb-8 text-gray-200"
                        },
                        "Keep track of your accomplishments each day of the workweek."
                    ),
                    React.createElement(
                        "div",
                        {
                            className: "my-8"
                        },
                        React.createElement(
                            "a",
                            {
                                className: "my-14 px-10 py-5 text-md font-bold tracking-wide text-center text-indigo-500  bg-white rounded-full hover:bg-blue-800 hover:text-white shadow-lg uppercase",
                                href: "/account"
                            },
                            "Get Started"
                        )
                    )
                )
            )
        );
    }
}

const domContainer = document.querySelector('#root');
ReactDOM.render(elem(Home), domContainer);
