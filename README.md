# PAM module for OAuth 2.0 Device Flow

PAM module for user authentication using
[OAuth 2.0 Device Authorization Grant](https://tools.ietf.org/html/rfc8628).

The following instructions have been tested on Ubuntu 20.04.

## Installation

Install build dependencies.

```bash
sudo apt install libldap2-dev libpam0g-dev libcurl4-openssl-dev
```

Clone the repository, build and install the module.

```bash
make
sudo mkdir /lib/security
sudo cp pam_oauth2_device.so /lib/security/
```

Create a configuration file `/etc/pam_oauth2_device/config.json`.
See `config_template.json` (LDAP section is optional).

### Configuration options

`config.json`

**qr** - allowed correction levels are

  * 0 - low
  * 1 - medium
  * 2 - high

**users** - user mapping. From claim configured in *username_attribute* to the local account name

### Example Configuration for sshd

Edit `/etc/pam.d/sshd`. Enable `pam_oauth2_device.so` and disable password
authentication.

```
auth required pam_oauth2_device.so /etc/pam_oauth2_device/config.json

# Standard Un*x authentication.
# @include common-auth
```

Edit `/etc/ssh/sshd_config`

```sshd-config
PasswordAuthentication no
ChallengeResponseAuthentication yes
AuthenticationMethods keyboard-interactive
UsePAM yes
```

It is also possible to combine multiple authentication methods. For example,
with `AuthenticationMethods publickey,keyboard-interactive`
both public key and interactive authentication are required.

For service users, an interactive method might not be desirable.
Specify alternative authentication methods for selected users.

```sshd-config
Match User ubuntu
  AuthenticationMethods publickey
```

Restart the service after changing the sshd configuration.

```bash
systemctl restart sshd
```

## Development

For local development it is easier to use `pamtester`.

### Installation

```bash
sudo apt install pamtester
```

### Configuration

Edit `/etc/pam.d/pamtester`

```
auth required pam_oauth2_device.so
```

### Deployment

```bash
sudo cp pam_oauth2_device.so /lib/security/
```

### Testing

```bash
sudo pamtester -v pamtester username authenticate
```
