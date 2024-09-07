#!/bin/bash
{
	log_file="./access.log"

	echo "Отчет о логе веб-сервера"
	echo "========================"

	total_requests=$(awk 'END{ print NR }' $log_file)
	echo  "Общее количество запросов:	$total_requests" 

	total_IP=$(awk '!seen[$1]++' $log_file | wc -l)
	echo  "Количество уникальных IP-адресов:	$total_IP"
	total_metod=$(awk '{split($6, method, "\""); print method[2]}' $log_file | sort | uniq -c
	echo "")
	echo ""

	echo "Количество запросов по методам:"
	echo "$total_metod"
	echo ""

	popular_URL=$(awk '{split($7, method, "\""); print method[1]}' $log_file | sort | uniq -c | sort -nr | head -n 1)
	echo "Самый популярный URL:	$popular_URL"
} > report.txt
echo "Отчет сохранен в файле report.txt"