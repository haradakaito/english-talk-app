import boto3
import os
import uuid
import base64
import time
import json

def lambda_handler(event, context):
    # 環境変数の読み込み
    model_id  = os.environ.get("BEDROCK_MODEL_ID")
    voice_id  = os.environ.get("POLLY_VOICE_ID")
    bucket    = os.environ.get("S3_BUCKET_NAME")
    lang_code = os.environ.get("TRANSCRIBE_LANGUAGE_CODE")

    # AWS SDKのクライアントを作成
    bedrock    = boto3.client("bedrock-runtime", region_name="ap-northeast-1")
    polly      = boto3.client("polly"          , region_name="ap-northeast-1")
    s3         = boto3.client("s3"             , region_name="ap-northeast-1")
    transcribe = boto3.client("transcribe"     , region_name="ap-northeast-1")

    return {
        "statusCode": 200,
        "body"      : json.dumps({"message": "Hello, World!"}),
        "headers"   : {"Access-Control-Allow-Origin": "*"}
    }

    # # 1. Speech to Text
    # audio_base64 = event.get("audio_base64")
    # if not audio_base64:
    #     return {
    #         "statusCode": 400,
    #         "body"      : json.dumps({"error": "audio_base64 is required"}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # audio_bytes = base64.b64decode(audio_base64)
    # audio_key   = f"chat-audio/input-{uuid.uuid4()}.mp3"
    # s3.put_object(
    #     Bucket = bucket,
    #     Key    = audio_key,
    #     Body   = audio_bytes,
    #     ContentType = "audio/mpeg"
    # )

    # job_name  = f"transcribe-{uuid.uuid4()}"
    # media_uri = f"s3://{bucket}/{audio_key}"

    # try:
    #     transcribe.start_transcription_job(
    #         TranscribeJobName = job_name,
    #         Media             = {"MediaFileUri": media_uri},
    #         MediaFormat       = "mp3",
    #         LanguageCode      = lang_code,
    #         OutputBucketName  = bucket
    #     )

    #     for _ in range(10):
    #         status = transcribe.get_transcription_job(
    #             TranscriptionJobName = job_name
    #         )
    #         if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    #             break
    #         elif status['TranscriptionJob']['TranscriptionJobStatus'] == 'FAILED':
    #             raise Exception("Transcription job failed")
    #         time.sleep(1)
    #     else:
    #         return {
    #             "statusCode": 500,
    #             "body"      : json.dumps({"error": "Transcription job timed out"}),
    #             "headers"   : {"Access-Control-Allow-Origin": "*"}
    #         }

    #     transcript_uri  = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    #     transcript_json = json.loads(boto3.client("s3").get_object(
    #         Bucket = bucket,
    #         Key    = f"{job_name}.json"
    #     )['Body'].read())

    #     transcribed_text = transcript_json['results']['transcripts'][0]['transcript']

    #     return {
    #         "statusCode": 200,
    #         "body"      : json.dumps({"input": transcribed_text}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # except Exception as e:
    #     return {
    #         "statusCode": 500,
    #         "body"      : json.dumps({"error": str(e)}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # # 2. Text to Text
    # prompt = "Hello! Can you understand me?"
    # body   = {
    #     "anthropic_version": "bedrock-2023-05-31",
    #     "messages"         : [{"role": "user", "content": prompt}],
    #     "max_tokens"       : 200,
    #     "temperature"      : 0.7
    # }

    # try:
    #     response = bedrock.invoke_model(
    #         modelId     = model_id,
    #         body        = json.dumps(body),
    #         contentType = "application/json",
    #         accept      = "application/json"
    #     )

    #     result = json.loads(response['body'].read())
    #     return {
    #         "statusCode": 200,
    #         "body"      : json.dumps({"input": prompt, "response": result['content'][0]['text']}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # except Exception as e:
    #     return {
    #         "statusCode": 500,
    #         "body"      : json.dumps({"error": str(e)}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # # 3. Text to Speech
    # prompt = "Yes, I can understand you. I am an artificial intelligence created by Anthropic to engage in conversation and assist with a variety of tasks. How can I help you today?"
    # key    = f"chat-audio/{uuid.uuid4()}.mp3"

    # try:
    #     response = polly.synthesize_speech(
    #         Text         = prompt,
    #         OutputFormat = "mp3",
    #         VoiceId      = voice_id,
    #     )

    #     audio_bytes = response['AudioStream'].read()
    #     s3.put_object(
    #         Bucket = bucket,
    #         Key    = key,
    #         Body   = audio_bytes,
    #         ContentType = "audio/mpeg"
    #     )

    #     signed_url = s3.generate_presigned_url(
    #         ClientMethod = "get_object",
    #         Params       = {"Bucket": bucket, "Key": key},
    #         ExpiresIn    = 600
    #     )

    #     return {
    #         "statusCode": 200,
    #         "body"      : json.dumps({"input": prompt, "audio_url": signed_url}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }

    # except Exception as e:
    #     return {
    #         "statusCode": 500,
    #         "body"      : json.dumps({"error": str(e)}),
    #         "headers"   : {"Access-Control-Allow-Origin": "*"}
    #     }
