using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public GameObject gameoverText; // 게임오버 시 활성화
    public Text timeText; // 생존시간 표시
    public Text recordText; // 최고기록 표시

    private float surviveTime; // 생존 시간
    private bool isGameover; //게임오버 상태

    void Start()
    {
        surviveTime = 0;
        isGameover = false;
    }

    void Update()
    {
        if(!isGameover) // 게임오버가 아닌 동안
        {
            surviveTime += Time.deltaTime; // 생존시간 갱신
            timeText.text = "Time : " + (int) surviveTime;
        }
        else
        {
            if (Input.GetKeyDown(KeyCode.R)) // 게임오버일 때 R 키 누름
            {
                SceneManager.LoadScene("SampleScene");
            }
        }
    }

    public void EndGame()
    {
        isGameover = true; // 현재 상태를 게임오버로 전환
        gameoverText.SetActive(true); // 게임오버 텍스트 활성화

        // 이전까지의 최고기록 가져오기
        float bestTime = PlayerPrefs.GetFloat("BestTime");

        // 이전까지의 최고기록보다 현재 생존 시간이 더 클 때
        if (surviveTime > bestTime)
        {
            bestTime = surviveTime; // 최고기록값을 현재 시간으로 변경
            
            // 변경된 최고기록을 저장
            PlayerPrefs.SetFloat("BestTime", bestTime);
        }

        // 최고기록 표시
        recordText.text = "Best Time : " + (int) bestTime;
    }
}
