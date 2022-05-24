# what is react
    React is a frontend and open-source JavaScript library 
    which is useful in developing user interfaces specifically for applications with a single page. 
    
    a single app usually consists of multiple components. reusable parts that can be processed separately.

    It splits the user interface into independent, 

## What is difference between React js and Angular js


# What is jsx, babel, webpack

## JSX 
    is a syntax extension to JavaScript we can write HTML structures in the same file that contains JavaScript code.

### Can web browsers read JSX directly? 
    For a web browser to read a JSX file, the file needs to be transformed into a regular JavaScript object using Babel

## babel


# DOM
    DOM stands for Document Object Model. 
    represents an HTML document with a logical tree structure. 
    Each branch of the tree ends in a node, and each node contains objects.


## What is the virtual DOM?
    react renderiza al Virtual DOM y no necesita cambiar todo el DOM como lo hace JS
    react no debe hacer usar el document por que va encontrar de el performance que ofrece
    Virtual DOM	React keeps a lightweight representation of the real DOM in the memory When the state of an object changes
    virtual DOM changes only that object in the real DOM rather than updating all the objects.


## ¿Cómo puedes optimizar el rendimiento de un componente en React?
    React updates only those components that have changed
    rather than updating all the components at once. 
    This results in much faster web applications.


# 2.- que es una SPA- FTA



# COMPONENTS

    Components are the building blocks of any React application whit essentially a piece of the user interface.  
    It splits the user interface into independent, reusable parts that can be processed separately.

## What is controlled and uncontrolled component in React js

    In a controlled component the value of the input element is controlled by React.
    Using event-based callbacks, any changes made to the input element will be reflected in the code as well.

    In an uncontrolled component the value of the input element is handled by the DOM itself.
    Input elements inside uncontrolled components work just like normal HTML input form elements.


## Difference between class component and function component

    Functional Components have no state of their own and only contain render methods and They may derive data from other components as props 


<br>

[Class Components](#react-antiguo)

    Class Components can hold and manage their own state and have a separate render method to return JSX on the screen. 

    They are also called Stateful components as they can have a state.
    What is pure component in React js

# What is a higher-order component in React?

    Higher-Order Component is a function that takes in a component and returns a new component. 

    Higher-Order Component helps to keep components simple and enables re-usability and keep our code don't repeat yuorself

    Higher-Order Component are generally used when multiple components have to use a common logic. 


    we want an abstraction that allows us to define this logic in a single place and share it across components. HOC allows us to create that abstraction.


# What is a state in React?

    Every component in react has a built in state object, which contains all the property values that belong to that component.

    the state object controls the behaviour of a component. 
    change in the property values of the state object leads to the re-rendering of the component.

    The state in a component can change over time and whenever it changes the component is re-renders.



## ¿Cómo puedes actualizar el estado de un componente en React?

    The useState is a built in React Hook that allows you for having state variables in functional components.
    
    It should be used when the DOM has something that is dynamically manipulating/controlling.

    We can make use of set method of useState for updating the state


## What is difference state and props in React js

## What is prop drilling in React js how to overcome it


# What are props in React?
    It is a React built in object that stores the value of attributes of a tag and works similarly to HTML attributes

    Using props we can pass data from one component to another.


<!-- Props are short for Properties. 
Props provide a way to pass data from one component to another component. Props are passed to the component in the same way as arguments are passed in a function.

The props in React are the inputs to a component of React. They can be single-valued or objects having a set of values that will be passed to components of React during creation by using a naming convention that almost looks similar to HTML-tag attributes. We can say that props are the data passed from a parent component into a child component.

The main purpose of props is to provide different component functionalities such as:

Passing custom data to the React component.
Using through this.props.reactProp inside render() method of the component.
Triggering state changes.
For example, consider we are creating an element with reactProp property as given below: <Element reactProp = "1" />
This reactProp name will be considered as a property attached to the native props object of React which already exists on each component created with the help of React library: props.reactProp;
 -->

## What is portal in React js

## What is context api in React js


# React antiguo

[componentes de clases](#components)

## What is super, constructor, render function in React js

## 20. What is the use of render() in React?

    render is required for each component class to have a render function for retun the html of our jsx
    
# Hooks in React js UseState, 

<!-- useMemo. useCallback -->

    Hooks are functions that let us hook into React state and lifecycle features from a functional component.

    React hooks were introduced in the 16.8 version of React. 
    
    Previously, functional components were called stateless components.
    
    Only class components were used for state management and lifecycle methods. 
    
    The need to change a functional component to a class component, whenever state management or lifecycle methods were to be used, led to the development of Hooks.

<!-- React Hooks must be called only at the top level. It is not allowed to call them inside the nested functions, loops, or conditions.
It is allowed to call the Hooks only from the React Function Components
React Hooks will allow you to use the state and other features of React in which requires a class to be written by you. In simple words, we can say that, React Hooks are the functions that will connect React state with the lifecycle features from the function components. React Hooks is among the features that are implemented latest in the version React 16.8. -->


## useEffect 

    The use Effect React Hook is used for performing the side effects in functional components.

    The use Effect hook will run by default after the first render and also after each update of the component.

    React will guarantee that the DOM will be updated by the time when the effect has run by it.

<!-- With the help of useEffect, you will inform React that your component requires something to be done after rendering the component or after a state change. The function you have passed(can be referred to as “effect”) will be remembered by React and call afterwards the performance of DOM updates is over. Using this, we can perform various calculations such as data fetching, setting up document title, manipulating DOM directly, etc, that don’t target the output value.

 -->

## What is useRef in React js

    The use Ref are used for managing focus media playback or text selection.

    The useRef Integrating with DOM libraries by third-party.
    Triggering the imperative animations.


# techniques to optimize React app performance.

    There are many ways through which one can optimize the performance of a React app, let’s have a look at some of them:

## Using useMemo( )

   
    
    By using useMemo the CPU Expensive function gets called only when it is needed

    use Memo hook can be used to cache such functions. 


<!-- It is a React hook that is used for caching CPU-Expensive functions.

Sometimes in a React app, a CPU-Expensive function gets called repeatedly due to re-renders of a component, which can lead to slow rendering. -->


## Using React.PureComponent 

    React.PureComponent is a base component class that checks the state and props of a component to know whether the component should be updated.

<!-- Instead of using the simple React.Component, we can use React.PureComponent to reduce the re-renders of a component unnecessarily. -->


## Maintaining State Colocation 
    This is a process of moving the state as close to where you need it as possible.
    Sometimes in React app, we have a lot of unnecessary states inside the parent component which makes the code less readable and harder to maintain. Not to forget, having many states inside a single component leads to unnecessary re-renders for the component.
    It is better to shift states which are less valuable to the parent component, to a separate component.
## Lazy Loading 
    Lazy Loading is a technique used to reduce the load time of a React app. 
    Lazy loading helps used to reduce the load time of web app performances to a minimum 


## What is useStrict in React js
    StrictMode is a tool of React to highlight potential problems in an application. It performs additional checks on the application.

### Identifying components with unsafe lifecycle methods: 
    Certain lifecycle methods are unsafe to use in asynchronous react applications. With the use of third-party libraries, it becomes difficult to ensure that certain lifecycle methods are not used.
    StrictMode helps in providing us with a warning if any of the class components use an unsafe lifecycle method.


### Warning about the usage of legacy string API:

    If one is using an older version of React, callback ref is the recommended way to manage refs instead of using the string refs. StrictMode gives a warning if we are using string refs to manage refs.

### Warning about the usage of findDOMNode:
    Previously, findDOMNode( ) method was used to search the tree of a DOM node. This method is deprecated in React. Hence, the StrictMode gives us a warning about the usage of this method.

### Warning about the usage of legacy context API (because the API is error-prone).

## What is fragment in React js


## What is node module in React js



## What are Custom Hooks?
    A Custom Hook is a function in Javascript whose name begins with ‘use’ and which calls other hooks. It is a part of React v16.8 hook update and permits you for reusing the stateful logic without any need for component hierarchy restructuring.

    In almost all of the cases, custom hooks are considered to be sufficient for replacing render props and HoCs (Higher-Order components) and reducing the amount of nesting required. Custom Hooks will allow you for avoiding multiple layers of abstraction or wrapper hell that might come along with Render Props and HoCs.

    The disadvantage of Custom Hooks is it cannot be used inside of the classes.


# 8. What is an event in React?
    An event is an action that a user or system may trigger  using camelCase rather than lowercase in HTML
    
    , such as pressing a key, a mouse click, etc.

    React events are named using camelCase, rather than lowercase in HTML.
    With JSX, you pass a function as the event handler, rather than a string in HTML.
    >`<Button onPress={lightItUp} />`

# 12. Why is there a need for using keys in Lists?

    A key is a unique identifier and it is used to identify which items have changed, been updated or deleted from the lists
    keys in Lists helps to determine which components need to be re-rendered instead of re-rendering all the components every time. Therefore, it increases performance, as only the updated components are re-rendered


# ¿Qué es React Router y cómo se puede utilizar para crear una SPA?
    React Router is a routing library built on top of React, which is used to create routes in a React application. 
    React Router is a routing library maintains consistent structure and behavior and is used to develop single page web applications. 
    Enables multiple views in a single application by defining multiple routes in the React application.


# What is Redux
    Redux is an open-source JavaScript library used to manage application State

    Redux is an open-source, JavaScript library used to manage the application state. 
    
    React uses Redux to build the user interface. It is a predictable state container for JavaScript applications and is used for the entire application’s state management.

    Store’s state is immutable
    Can only have a single-store
    Uses the concept of reducer


### What is reducer, action, store in Redux
    Store Holds the state of the application Action is the source information for the store Reducer Specifies how the applications state changes in response to actions sent to the store.



### Explain data flow in Redux

### What is middleware in Redux

### Redux-thunk and Redux-saga Difference between


# What is the Flux?

    Flux is an architecture and not a framework or librarythat Facebook uses for building web applications. 

    It is a method of handling complex data inside a client-side application and manages how data flows in a React application.
    
    There is a single source of data (the store) and triggering certain actions is the only way way to update them.

### Explain data flow in Flux

    The actions call the dispatcher, and then the store is triggered and updated with their own data accordingly.

    When a dispatch has been triggered, and the store updates, it will emit a change event that the views can rerender accordingly.

    
    Store’s state is mutable
    Can have multiple stores
    Uses the concept of the dispatcher


# What is reconciliation in React js
# What is server side render in React js
# What is the default localhost server port in react js. :3000
## how can we change the local server port





