const KEY='phychem-study-v1';
export type Store={theme?:'light'|'dark';completed:string[];bookmarkedFormulas:string[];bookmarkedProblems:string[];attempts:{problemId:string;correct:boolean;at:string}[];flashcards:Record<string,{interval:number;due:string;reviews:number}>};
const empty:Store={completed:[],bookmarkedFormulas:[],bookmarkedProblems:[],attempts:[],flashcards:{}};
export function loadStore():Store{try{return {...empty,...JSON.parse(localStorage.getItem(KEY)||'{}')}}catch{return empty}}
export function saveStore(store:Store){localStorage.setItem(KEY,JSON.stringify(store));window.dispatchEvent(new Event('study-store'))}
export function schedule(current:Store['flashcards'][string]|undefined,known:boolean){const reviews=(current?.reviews||0)+1;const interval=known?Math.max(1,(current?.interval||0)*2||1):0;const due=new Date(Date.now()+(known?interval:0)*86400000).toISOString();return{interval,due,reviews}}
