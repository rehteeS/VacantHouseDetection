// グローバル変数
var streetViewPanorama ;

// 初期化用の関数
function initFunc (lat, lng) {
	// キャンパスの要素を取得する
	var canvas = document.getElementById( 'map-canvas' ) ;

	// 返り値の案内を空にする
	returnFunc( "" ) ;

	// 地図のインスタンスを作成する
	streetViewPanorama = new google.maps.StreetViewPanorama( canvas, {
		position: new google.maps.LatLng( lat, lng ) ,
	} ) ;
} ;

// メソッドボタンのイベント
document.getElementById( "method" ).onclick = function () {
	// 実行
	var result = streetViewPanorama.getLinks() ;

	// 返り値をコンソールに表示
	console.log( "返り値:", result ) ;

	// 返り値を表示
	returnFunc( result ) ;
}

// リセットボタンのイベント
document.getElementById( "reset" ).onclick = initFunc ;

// 返り値表示用の関数
function returnFunc ( value ) {
	switch ( typeof value ) {
		case "undefined" :
			value = "undefined" ;
		break ;

		case "null" :
			value = "null" ;
		break ;

		case "object" :
			try {
				value = JSON.stringify( value ) ;
			} catch (e) {
			}
		break ;
	}

	document.getElementById( "return" ).textContent = value.toString() ;
}

/* getLinks()の戻り値は、JSON化されていないので、JSON.stringifyを使ってJSON化する */
function GL() {
	var result = JSON.stringify(streetViewPanorama.getLinks());
	return result;
}


// 地図の表示開始
//initFunc() ;
