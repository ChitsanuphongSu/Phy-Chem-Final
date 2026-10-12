import{AnalyticsPanels}from'./Phase7C';import ProgressPortability from'./ProgressPortability';import type{Store}from'./storage';
export default function DashboardExtras({store}:{store:Store}){return <><AnalyticsPanels store={store}/><ProgressPortability/></>}
