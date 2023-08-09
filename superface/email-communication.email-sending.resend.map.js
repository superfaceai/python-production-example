function SendEmail({input, parameters, services}){
  const url = `${services.default}/email`;
const options = {
  method: 'POST',
  body: {
    to: input.to,
    from: input.from,
    subject: input.subject,
    bcc: input.bcc,
    cc: input.cc,
    reply_to: input.reply_to,
    html: input.html,
    text: input.text,
  },
  headers: {
    'Content-Type': 'application/json',
  },
  security: 'bearerAuth',
};

const response = std.unstable.fetch(url, options).response();
const body = response.bodyAuto() ?? {};

if (response.status !== 200) {
  const error = {
    error: {
      code: response.status,
      message: response.headers['error-message']?.[0] ?? 'Unknown error',
      details: {
        invalid_email: response.headers['invalid-email']?.[0],
      },
    },
  };
  throw new std.unstable.MapError(error);
}

const result = {
  id: body.id,
  from: body.from,
  to: body.to,
  created_at: body.created_at,
};

return result;
}