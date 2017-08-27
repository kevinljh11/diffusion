from sys import argv

from twisted.internet import reactor

from modules import diffusion


def main():
        bet365()
        reactor.run()
        return

def bet365():
    topics = [
        '__host',
        'CONFIG_1_3',
        'OVInPlay_1_3',
    ]
    diffusion_client = diffusion.DiffusionClient(
        'wss://premws-pt1.365lpodds.com/zap/',
        '1',
        session_url='https://www.bet365.com/',
        protocol='zap-protocol-v1',
        headers={},
        topics=topics,
    )
    if diffusion_client.can_connect():
        try:
            diffusion_client.connect()
        except KeyboardInterrupt:
            diffusion_client.disconnect()
        except Exception:
            diffusion_client.disconnect()

if __name__ == '__main__':
    main()
