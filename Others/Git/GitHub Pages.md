- Deploy Github
    
    ### add token for deploy
    
    
    ### install gh-pages
    
    ```$ npm install gh-pages```
    
    package.json
    
    ```json
    {
      "name": "cripto",
      "version": "0.1.0",
      "private": true,
      "homepage": "https://your_user.github.io/your_repo/", //add this
      "dependencies": {
        "@testing-library/jest-dom": "^5.16.2",
    ```
    
    ```json
    "web-vitals": "^2.1.4"
      },
      "scripts": {
        "predeploy":"npm run build",    //add this
        "deploy":"gh-pages -d build",   //add this
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
    ```
    
`$ npm run deploy`