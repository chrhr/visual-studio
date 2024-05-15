using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public GameObject gameoverText; // ���ӿ��� �� Ȱ��ȭ
    public Text timeText; // �����ð� ǥ��
    public Text recordText; // �ְ��� ǥ��

    private float surviveTime; // ���� �ð�
    private bool isGameover; //���ӿ��� ����

    void Start()
    {
        surviveTime = 0;
        isGameover = false;
    }

    void Update()
    {
        if(!isGameover) // ���ӿ����� �ƴ� ����
        {
            surviveTime += Time.deltaTime; // �����ð� ����
            timeText.text = "Time : " + (int) surviveTime;
        }
        else
        {
            if (Input.GetKeyDown(KeyCode.R)) // ���ӿ����� �� R Ű ����
            {
                SceneManager.LoadScene("SampleScene");
            }
        }
    }

    public void EndGame()
    {
        isGameover = true; // ���� ���¸� ���ӿ����� ��ȯ
        gameoverText.SetActive(true); // ���ӿ��� �ؽ�Ʈ Ȱ��ȭ

        // ���������� �ְ��� ��������
        float bestTime = PlayerPrefs.GetFloat("BestTime");

        // ���������� �ְ��Ϻ��� ���� ���� �ð��� �� Ŭ ��
        if (surviveTime > bestTime)
        {
            bestTime = surviveTime; // �ְ��ϰ��� ���� �ð����� ����
            
            // ����� �ְ����� ����
            PlayerPrefs.SetFloat("BestTime", bestTime);
        }

        // �ְ��� ǥ��
        recordText.text = "Best Time : " + (int) bestTime;
    }
}
