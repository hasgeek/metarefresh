$(function(){$(".leaflet-map").each(function(){var e,a,o,t,r=$(this),m={zoom:5,marker:[12.9833,77.5833],label:null,maxZoom:18,attribution:'<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/" target="_blank">CC-BY-SA</a>',subdomains:["a","b","c"],scrollWheelZoom:!1};r.empty(),e=r.data(),e.marker&&(e.marker=e.marker.split(",")),a=$.extend({},m,e),o=new L.Map(r[0],{center:a.center||a.marker,zoom:a.zoom,scrollWheelZoom:a.scrollWheelZoom}),L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",{maxZoom:a.maxZoom,attribution:a.attribution,subdomains:a.subdomains}).addTo(o),t=new L.marker(a.marker).addTo(o),a.label&&t.bindPopup(a.label).openPopup()})});