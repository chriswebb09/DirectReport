const { useState, useEffect } = React;

const RememberMe = () => {
    return (
        <div className="flex items-start">
            <div className="flex items-center h-5">
                <input id="remember" name="remember" aria-describedby="remember" type="checkbox" className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" required=""/>
            </div>
            <div className="ml-3 text-sm">
                <label htmlFor="remember" className="text-white dark:text-gray-300">
                    Remember me
                </label>
            </div>
        </div>
    )
}

const NameElement = (props) => {
    return (
        <div>
            <label htmlFor={props.forHtml} className="block mb-2 text-sm font-semibold tracking-wider text-white dark:text-white">
                {props.labelText}
            </label>
            <input type={props.type} name={props.name} id={props.id} className="bg-gray-50 border border-gray-300 text-blue-500 tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-semibold" placeholder={props.placeholder} required="" value={props.value}/>
        </div>
    )
}

const AccountForm = ({action, submit_button}) => {
    console.log(action);
    console.log(submit_button);
    let props;
    return (
        <form className="space-y-4 md:space-y-6" method="POST" action={action}>
            {NameElement(props = {
                type: "email",
                forHtml: "email",
                labelText: "Email",
                name: "email",
                id: "email",
                placeholder: "name@company.com",
                value: "name@company.com"
            })}
            {NameElement(props = {
                type: "text",
                forHtml: "firstname",
                labelText: "First name",
                name: "firstname",
                id: "firstname",
                placeholder: "John",
                value: "John"
            })}
            {NameElement(props = {
                type: "text",
                forHtml: "lastname",
                labelText: "Last name",
                name: "lastname",
                id: "lastname",
                placeholder: "Doe",
                value: "Doe"
            })}
            {NameElement(props = {
                type: "text",
                forHtml: "username",
                labelText: "Username",
                name: "username",
                id: "username",
                placeholder: "JohnDoe",
                value: "JohnDoe"
            })}
            {NameElement(props = {
                type: "password",
                forHtml: "password",
                labelText: "Password",
                name: "password",
                id: "password",
                placeholder: "••••••••",
                value: "••••••••"
            })}
            <div className="flex items-center justify-between">
                {RememberMe()}
            </div>
            <button type="submit" className="w-full text-white bg-sky-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                {submit_button}
            </button>
        </form>
    )
}

const UserAccount = ({action, header, button_title}) => {
    return (
        <div>
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div className="w-full bg-blue-500 rounded-3xl shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                            {header}
                        </h1>
                        {AccountForm({action}, {button_title})}
                    </div>
                </div>
            </div>
        </div>
    )
}
