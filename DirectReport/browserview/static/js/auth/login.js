const { useState, useEffect } = React;

const LoginForm = () => {
     return (
         <div className="flex flex-col items-center justify-center px-6 py-20 mx-auto md:h-90 lg:py-220">
             <div className="w-full bg-blue-500 rounded-3xl shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700 rounded-3xl shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)]">
                 <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                     <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                         Sign in to your account
                     </h1>
                     <form className="space-y-4 md:space-y-6" method="POST" action="/login">
                         <div>
                             <label htmlFor="email" className="block mb-2 text-sm font-medium text-white dark:text-white">Your email</label>
                             <input type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] " placeholder="name@company.com" required=""/>
                         </div>
                         <div>
                             <label htmlFor="password" className="block mb-2 text-sm font-medium text-white dark:text-white">
                                 Password
                             </label>
                             <input type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-white sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] " required=""/>
                         </div>
                         <div className="flex items-center justify-between">
                             <div className="flex items-start">
                                 {RememberMe()}
                             </div>
                             <a href="#" className="text-sm font-medium text-white hover:underline dark:text-primary-500">
                                 Forgot password?
                             </a>
                         </div>
                         <button type="submit" className="w-full text-white bg-sky-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] ">
                             Sign in
                         </button>
                         {/*<button className="w-80 sm:w-90 bg-white hover:bg-blue-400 text-blue-500 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-3xl mt-2" type="button">*/}
                         {/*    <a className="btn btn-primary" href="/authorize/github">Login with GitHub</a>*/}
                         {/*</button>*/}
                         <p className="text-sm font-light text-white dark:text-gray-400 ml-14">Don’t have an account yet?
                             <a href="/signup" className="font-medium text-gray-200 ml-3 hover:underline dark:text-primary-500">Sign up</a>
                         </p>
                     </form>
                 </div>
             </div>
         </div>
     )
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<LoginForm/>, domContainer);