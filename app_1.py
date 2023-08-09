import requests

# Criar um perfil personalizado
create_profile_url = "http://127.0.0.1:5555/create-profile-custom"

headers = {
    "Content-Type": "application/json"
}

profile_data = {
    "os": "win",
    "version": "113.0.5615.204",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5615.183 Safari/537.36",
    "canvas": "noise",
    "webGLImage": True,
    "audioContext": True,
    "webGLMetadata": True,
    "clientRectsEnable": True,
    "noiseFont": True,
    "webGLVendor": "Google Inc. (Intel)",
    "webGLMetadataRenderer": "ANGLE (Intel, Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11-21.20.16.4526)",
    "StartURL": "",
    "languages": "en-us,vi;q=0.9",
    "resolution": "1024x768"
}

create_response = requests.post(create_profile_url, json=profile_data, headers=headers)

if create_response.status_code == 200:
    create_result = create_response.json()
    if create_result["type"] == "success":
        content_information = create_result["content"]
        print("Profile created successfully.")
        print("Content information:", content_information)

        # Extrair informações relevantes do conteúdo
        profile_uuid = content_information["uuid"]
        proxy_info = ""
        command = ""

        # Construir a URL para abrir o perfil
        api_base_url = f"http://127.0.0.1:5555/openProfile?uuid={profile_uuid}"

        # Verificar se o proxy_info está presente e não é vazio
        if proxy_info:
            api_base_url += f"&proxy={proxy_info}"

        # Verificar se o command está presente e não é vazio
        if command:
            api_base_url += f"&command={command}"

        # Realizar a solicitação GET para abrir o perfil
        open_response = requests.get(api_base_url)

        if open_response.status_code == 200:
            open_result = open_response.json()
            print(open_result)
            if open_result["status"] == "successfully":
                remote_port = open_result["data"]["remote_port"]
                profile_path = open_result["data"]["profile_path"]
                execute_path = open_result["data"]["execute_path"]
                print(f"Perfil com UUID {profile_uuid} foi aberto com sucesso.")
                print(f"Remote Port: {remote_port}")
                print(f"Profile Path: {profile_path}")
                print(f"Execute Path: {execute_path}")
            else:
                print("Falha ao abrir o perfil.")
        else:
            print("Solicitação para abrir o perfil falhou com código de status:", open_response.status_code)



