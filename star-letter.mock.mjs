// Development host handlers only. This file is excluded from dist/.
import {readFile,writeFile,rename} from 'node:fs/promises';
const file=new URL('./.star-letter-preview-store.json',import.meta.url);let data={};
try{data=JSON.parse(await readFile(file,'utf8'));}catch(e){if(e.code!=='ENOENT')throw e;}
let pending=Promise.resolve();
function commit(action){const job=pending.then(async()=>{const result=action();const temporary=new URL('./.star-letter-preview-store.tmp',import.meta.url);await writeFile(temporary,JSON.stringify(data));await rename(temporary,file);return result;});pending=job.catch(()=>{});return job;}
export default {
 'storage.get':async({key,scope='user'})=>{await pending;const a=data[scope+':'+key];return {value:a?.value??null,version:a?.version??0};},
 'storage.set':async({key,value,scope='user',ifVersion})=>commit(()=>{const id=scope+':'+key,old=data[id];if(ifVersion!==undefined&&ifVersion!==(old?.version??0))throw Object.assign(Error('STORAGE_CONFLICT'),{code:'STORAGE_CONFLICT'});const version=(old?.version??0)+1;data[id]={value,version,updateTime:Date.now()};return {ok:true,version};}),
 'storage.del':async({key,scope='user'})=>commit(()=>{delete data[scope+':'+key];return {ok:true};}),
 'storage.list':async({prefix='',scope='user'})=>{await pending;return {keys:Object.entries(data).filter(([key])=>key.startsWith(scope+':'+prefix)).map(([key,a])=>({key:key.slice(scope.length+1),version:a.version,size:Buffer.byteLength(JSON.stringify(a.value)),updateTime:a.updateTime}))};},
};
