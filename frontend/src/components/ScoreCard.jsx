import React from "react";

const ScoreCard = ({ title, score }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold text-gray-700">
        {title}
      </h3>

      <p className="text-4xl font-bold text-blue-600 mt-3">
        {score}
      </p>
    </div>
  );
};

export default ScoreCard;