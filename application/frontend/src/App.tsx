import { useState, useEffect } from 'react'

import api from './api'


export default function App() {
    const [ count, setCount ] = useState(0)

    const fetchCount = async (): Promise<number> => {
        let response = await api.get("/requests")
        const data = response.data
        return data.count
    }

    useEffect(() => {
        const loadCount = async () => {
            const count = await fetchCount()
            setCount(count)
        }
        loadCount()
    }, [])

    return (
        <div>
            <h1>Request count: {count}</h1>
        </div>
    )
}
