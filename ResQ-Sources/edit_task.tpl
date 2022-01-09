%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<head>
    <title>Configuration Portal - ResQ Systems</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    html {
        height: 100%;
    }

    h4{
		font-family: "Lucida Console", "Courier New", monospace;
	}

    body {
        height: 100%;
        margin: 0;
        padding: 0;
        	 background: linear-gradient(90deg, #fff6e3 21px, transparent 1%) center, linear-gradient(#fff6e3 21px, transparent 1%) center, #ffffff;
	 background-size: 22px 22px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .main {
        position: relative;
    }

    .dragon {
        width: 200px;
        height: 140px;
        transform-origin: 50% 80%;
        animation: zoomIn .5s cubic-bezier(0.47, 0, 0.75, 0.72) infinite alternate;
    }

    .dragon .body {
        
        margin: auto;
		width: 50%;
		padding: 5px;
		height: 180px;
        background: url('https://nine4tech.bss.design/assets/img/ResQ.png?h=1ecc380f055aa3f9b681586d4a281ed0') no-repeat center center;
        background-size: contain;
        
    }

    .dragon .horn-left {
        position: absolute;
        top: -17px;
        left: 32px;
        width: 31px;
        height: 31px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/horn-left.png?raw=true') no-repeat;
        background-size: contain;
        z-index: 9;
        transform-origin: 150% 200%;
        transform: rotate(-5deg);
        animation: swingRight .5s cubic-bezier(0.47, 0, 0.75, 0.72) infinite alternate;
    }

    .dragon .horn-right {
        position: absolute;
        top: -16px;
        left: 110px;
        width: 34px;
        height: 31px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/horn-right.png?raw=true') no-repeat;
        background-size: contain;
        z-index: 9;
        transform-origin: -50% 200%;
        transform: rotate(5deg);
        animation: swingLeft .5s cubic-bezier(0.47, 0, 0.75, 0.72) infinite alternate;
    }

    .dragon .eye {
        position: absolute;
        top: 39px;
        width: 11px;
        height: 11px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/eye.png?raw=true') no-repeat;
        background-size: contain;
        z-index: 12;
    }

    .dragon .eye.left {
        left: 49px;
    }

    .dragon .eye.right {
        left: 118px;
        transform-origin: 50% 50%;
        transform: rotate(180deg);
    }

    .dragon .blush {
        position: absolute;
        top: 46px;
        width: 15px;
        height: 9px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/blush.png?raw=true') no-repeat;
        background-size: 100% 100%;
        z-index: 11;
        animation: blush .5s ease infinite alternate;
    }

    .dragon .blush.left {
        left: 43px;
    }

    .dragon .blush.right {
        left: 120px;
    }

    .dragon .mouth {
        position: absolute;
        top: 52px;
        left: 49px;
        width: 78px;
        height: 56px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/mouth.png?raw=true') no-repeat;
        background-size: 100%;
        z-index: 11;
        animation: openMouth 1s ease infinite;
    }

    .dragon .tail-sting {
        position: absolute;
        top: 67px;
        left: 139px;
        width: 40px;
        height: 38px;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/tail-sting.png?raw=true') no-repeat;
        background-size: contain;
        z-index: 9;
        transform-origin: 0 100%;
        animation: tailUp .5s cubic-bezier(0.47, 0, 0.75, 0.72) infinite alternate;
    }

    .shadow-wrapper {
        position: absolute;
        top: 110px;
        width: 100%;
    }

    .shadow {
        margin: 0 auto;
        width: 110px;
        height: 30px;
        background: rgba(0, 0, 0, 0.15);
        border-radius: 50%;
        z-index: 0;
        animation: zoomIn .5s cubic-bezier(0.47, 0, 0.75, 0.72) infinite alternate;
    }

    .fire-wrapper {
        position: absolute;
        width: 40px;
        top: 60px;
        left: 88px;
        transform: translate(-50%, -50%);
        transform-origin: 50% 100%;
        animation: fireUp 1s ease-in infinite;
    }

    .fire {
        padding-bottom: 135%;
        width: 100%;
        height: 100%;
        background: url('https://github.com/devyumao/dragon-loading/blob/master/img/fire.png?raw=true') no-repeat;
        background-size: contain;
        animation: fire 1s ease-out infinite;
    }

    .progress {
        margin-top: 30px;
        width: 100%;
    }

    .progress .outer {
        width: 100%;
        height: 14px;
        border-radius: 7px;
        background: rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }

    .progress .inner {
        width: 0;
        height: 100%;
        background: #ff2b5d;
        animation: loading 2s linear infinite;
    }

    @keyframes zoomIn {
        100% {
            transform: scale(1.16, 1.16);
        }
    }

    @keyframes swingRight {
        100% {
            transform: rotate(5deg);
        }
    }

    @keyframes swingLeft {
        100% {
            transform: rotate(-5deg);
        }
    }

    @keyframes blush {
        0% {
            opacity: 0;
        }

        100% {
            opacity: 1;
        }
    }

    @keyframes openMouth {
        0% {
            -webkit-clip-path: ellipse(20% 0% at 50% 0);
                    clip-path: ellipse(20% 0% at 50% 0);
        }

        50% {
            -webkit-clip-path: ellipse(100% 100% at 50% 0);
                    clip-path: ellipse(100% 100% at 50% 0);
        }

        70% {
            -webkit-clip-path: ellipse(100% 100% at 50% 0);
                    clip-path: ellipse(100% 100% at 50% 0);
        }

        100% {
            -webkit-clip-path: ellipse(20% 0% at 50% 0);
                    clip-path: ellipse(20% 0% at 50% 0);
        }
    }

    @keyframes tailUp {
        0% {
            transform: scaleY(0.9);
        }

        100% {
            transform: scaleY(1.06);
        }
    }

    @keyframes loading {
        100% {
            width: 100%;
        }
    }

    @keyframes fireUp {
        0% {
            top: 70px;
        }

        20% {
            top: 70px;
        }

        100% {
            top: -80px;
        }
    }

    @keyframes fire {
        0% {
            transform: scale(0, 0);
            opacity: 0.8;
        }

        20% {
            transform: scale(0, 0);
            opacity: 0.8;
        }

        50% {
            opacity: 0.8;
        }

        100% {
            transform: scale(1, 1);
            opacity: 0;
        }
    }
    </style>
</head>
<body>	
    <div class="main">
        <div class="shadow-wrapper">
            <div class="shadow"></div>
        </div>
        <div class="dragon">
            <div class="body"></div>
        </div>
        <div class="fire-wrapper">
            <div class="fire"></div>
        </div>
        <div class="progress">
            <div class="outer">
                <div class="inner"></div>
            </div>
            <br><h4><a href="/login"><center>Update Database</center></a></h4>
        </div>
    </div>
</body>

