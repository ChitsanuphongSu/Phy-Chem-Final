import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, HashRouter } from 'react-router-dom';
import 'katex/dist/katex.min.css';
import './styles.css';
import App from './App';
const basename=import.meta.env.BASE_URL==='./'?'/':import.meta.env.BASE_URL;
const router=import.meta.env.BASE_URL==='./'?<BrowserRouter basename={basename}><App/></BrowserRouter>:<HashRouter><App/></HashRouter>;
ReactDOM.createRoot(document.getElementById('root')!).render(<React.StrictMode>{router}</React.StrictMode>);
