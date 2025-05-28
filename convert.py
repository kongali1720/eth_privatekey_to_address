from eth_account import Account

def convert_private_key_to_address(private_key):
    try:
        acct = Account.from_key(private_key)
        print("✅ Ethereum Address:", acct.address)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    print("🔑 Konversi Private Key ke Ethereum Address")
    private_key = input("Masukkan private key (tanpa 0x): ").strip()
    convert_private_key_to_address("0x" + private_key)
