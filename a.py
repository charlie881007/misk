import pyautogui
import time
import win32con
import win32clipboard
import random

text_template = """function clickfloat(){
    document.getElementById("allfloatbutton").click();
}

function buy(){
    console.log(document.querySelector("#market_buynow_dialog_purchase").children[0]);
    document.querySelector("#market_buynow_dialog_purchase").children[0].click();
}

function findTarget(){
    let priceCap = 14.5;
    let floatCap = 0.0231;

    let blocks = document.querySelectorAll(".market_listing_row");

    for (var i = 0; i < blocks.length; i++){
        let element = blocks[i];
        let float = element.querySelector(".value");
        let price = element.querySelector(".market_listing_price_with_fee");

		if (float){
			float = float.innerHTML;
            float = parseFloat(float);
            price = price.innerHTML.replace("NT$ ", "");
            price = parseFloat(float);

            console.log(float);

			if (float < floatCap && price < priceCap){
                let buyBtn = element.querySelector(".item_market_action_button")
                console.log("找到目標")

				if (buyBtn){
                    console.log("下單中")

					buyBtn.click()	

					document.querySelector("#market_buynow_dialog_accept_ssa").checked = true;	
					setTimeout(buy, 100);
				}
			}
        }
    }
}

function reload(){
    history.go(0);
}

function main(){
// 按按鈕
    setTimeout(clickfloat, 500);

	// 找符合的
    setTimeout(findTarget, 2200);

    // 刷新 
    setTimeout(reload, _sec);
}

main();
"""


def copy(text):
    """複製"""
    win32clipboard.OpenClipboard()  # 開啟剪貼簿
    win32clipboard.EmptyClipboard()  # 清空剪貼簿內容。可以忽略這步操作，但是最好加上清除貼上板這一步
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)  # 以Unicode文字形式放入剪下板
    win32clipboard.CloseClipboard()  # 關閉剪貼簿


def main():

    time.sleep(10)

    while True:
        sec = random.randint(7, 10)
        text = text_template.replace("_sec", str(sec*1000))

        copy(text)

        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        time.sleep(sec+2)


main()