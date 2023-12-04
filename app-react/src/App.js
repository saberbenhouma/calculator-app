import React, { useState } from 'react';

const App = () => {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);

  const calculate = async () => {
    try {
      const response = await fetch('http://localhost:8000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression }),
      });

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error calculating:', error);
    }
  };

  const exportToCSV = async () => {
    try {
      const response = await fetch('http://app-python:8000/export_csv');

      // Traiter les données CSV ou les télécharger si nécessaire
    } catch (error) {
      console.error('Error exporting to CSV:', error);
    }
  };

  return (
    <div>
      <h1>Calculator App</h1>
      <input
        type="text"
        value={expression}
        onChange={(e) => setExpression(e.target.value)}
      />
      <button onClick={calculate}>Calculate</button>
      {result !== null && <p>Result: {result}</p>}
      <button onClick={exportToCSV}>Export to CSV</button>
    </div>
  );
};

export default App;
