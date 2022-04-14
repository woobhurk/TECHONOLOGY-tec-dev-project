- __readme
- **前提**
    - 已搭建好 Jenkins 平台；
    - 宿主服务器上有 Docker。
- **文件介绍**
    - `Dockerfile`
        - Docker 构建文件。
    - `docker-project-run.sh`
        - 构建 Docker 镜像。
        - 使用方式为：

            ```shell
            docker-project-run.sh {{镜像名}} {{镜像端口}} {{宿主机端口}} {{JAR 文件路径}}
            ```

        - 命令介绍：
            - `{{镜像名}}`：即 Docker 镜像名称。
            - `{{镜像端口}}`：镜像中需要映射到宿主机的端口号。
            - `{{宿主机端口}}`：需要映射到的宿主机的端口号，可以为多个，需要用 `"PORT1 PORT2"` 这种形式指定。
            - `{{JAR 文件路径}}`：项目文件的路径。

    - `docker-project-entrypoint.sh`
        - Docker 容器的入口，可以编辑这个脚本，在里面增加一些需要在容器启动时的命令，如修改 `/etc/hosts` 文件。
- **使用方式**
    - 假设宿主服务器的项目目录为 `/data/project/`；
    - 先将这三个文件复制过去，然后执行命令；
    - `docker-project-run.sh` 会将 `{{JAR 文件路径}}` 所在的目录设置成 Docker 的上下文目录，同时将目录中的所有文件一并复制到 Docker 容器中；
    - 生成的容器名称为 `{{镜像名}}-{{端口号}}`。
