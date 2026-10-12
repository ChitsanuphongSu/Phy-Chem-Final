import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import 'katex/dist/katex.min.css';
import './styles.css';
import App from './App';
const basename=import.meta.env.BASE_URL==='./'?'/':import.meta.env.BASE_URL;
ReactDOM.createRoot(document.getElementById('root')!).render(<React.StrictMode><BrowserRouter basename={basename}><App/></BrowserRouter></React.StrictMode>);
