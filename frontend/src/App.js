import React from 'react';
import './App.css';

import { getName } from "country-list";
import { VectorMap } from "react-jvectormap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes, faQuestionCircle } from '@fortawesome/free-solid-svg-icons';
import Ticker from 'react-ticker';
 
// const ReactHeatmap = require("react-heatmap");

// const data = [{ x: 10, y: 15, value: 5}, { x: 50, y: 50, value: 2}];

// const mapData = {
//   CN: 100000,
//   IN: 9900,
//   SA: 86,
//   EG: 70,
//   SE: 0,
//   FI: 0,
//   FR: 0,
//   US: 20,
// };

class App extends React.Component {
  state = {
    currentCountry: ""
  }
  countryClick = (e, countryCode) => {
    e.preventDefault();
    let tips = document.getElementsByClassName("jvectormap-tip");
    for (let i = 0; i < tips.length; i++) {
      tips[i].style.display = "none";
    }
    this.setState({
      currentCountry: getName(countryCode)
    });
  };
  closeWindow = () => {
    this.setState({
      currentCountry: ""
    });
  }
  render() {
    return (
      <div className="App">
        <VectorMap
          updateSize
          map={"world_mill"}
          backgroundColor="#2B2B2B"
          zoomOnScroll={false}
          containerStyle={{
            width: "100%",
            height: window.innerHeight
          }}
          onRegionClick={this.countryClick}
          containerClassName="map"
          regionStyle={{
            initial: {
              // fill: "#E8E8E8",
              fill: "#777777",
              "fill-opacity": 0.9,
              stroke: "#000",
              "stroke-width": 0,
              "stroke-opacity": 0
            },
            hover: {
              "fill-opacity": 0.8,
              cursor: "pointer"
            },
            selected: {
              fill: "#2938bc"
            },
            selectedHover: {}
          }}
          regionsSelectable={true}
          // series={{
          //   regions: [
          //     {
          //       values: mapData,
          //       scale: ["#146804", "#ff0000"],
          //       normalizeFunction: "polynomial"
          //     }
          //   ]
          // }}
        />
        <div className="country-headline-container" style={{display: this.state.currentCountry ? "block" : "none" }}>
          <FontAwesomeIcon icon={faTimes} onClick={this.closeWindow} />
          <h2 className="country-title">{ this.state.currentCountry }</h2>
          <h3 className="headline">Protest in Chile lol</h3>
        </div>
        {/* <div className="global-headline-container">
          <h2 className="country-title">Global Headlines</h2>
          <h3 className="headline">Protest in Chile lol</h3>
        </div> */}
        <Ticker>
          {({ index }) => (
            <>
            <p>This is a new piece of news bro                  This is a new piece of news bro</p>
            </>
          )}
        </Ticker>
        <FontAwesomeIcon icon={faQuestionCircle}/>
      </div>
    );
  }
}

export default App;