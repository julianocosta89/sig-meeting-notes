SIG: Sampling SIG
Date: 2025-11-06
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/asBhh5e6C12JU2HhdXHh5V23EYMDFGAp12PW02atE4UpNhq348bBz4txokwUMgCG.7BTihvHtf4QmYMOq
============================================================

## Zoom Recording Transcript

**Kent Quirk (he/him)** 03:49 Without an agenda, I say we give it 2 more minutes, and… Beg it.
Unless somebody has something they need to talk about.
**Peter Findeisen** 04:03 Nothing from my side.
**Kent Quirk (he/him)** 04:07 They shared this with me.
**Otmar Ertl (Dynatrace)** 04:10 Also, not from our side.
**Kent Quirk (he/him)** 04:13 Yeah, I don't have anything either.
Oh, here he is.
**Joshua MacDonald** 04:25 Hello, friends.
**Peter Findeisen** 04:27 Hello.
**Kent Quirk (he/him)** 04:27 We were just noting that we don't have an agenda.
**Joshua MacDonald** 04:30 I was gonna say, I don't care about… And I don't have one.
But I came to say hello.
if you ask me to make one up, which I'm not sure you are, the topic of declarative configuration has been on my mind lately.
looking at how metrics and logs and so on, like.
there's something there, and I know that we've thought about and talked about
Considering extensions on the declarative config to support composable samplers.
I know it's a lot to ask for. It's just been on my mind a little bit, if I'd mention it.
we're looking at how to configure the Rust SDK right now, and it doesn't support declarative configuration at all.
But it's like, sometimes within OpenTelemetry, you see things that…
maybe it's not exactly the way you'd implement something or design something yourself, but it is what it is, it's there, it's done. So, looking at the views configuration and declarative configuration for metrics, not entirely loving what I see, but it's there, and I can't necessarily argue with it.
If we had something like that for sampling, I think it would make sense.
Probably… probably be hard to read.
confusing, and I actually don't think users really want to enter those configurations, but.
**Kent Quirk (he/him)** 06:01 There's value in it, and the thing we're seeing a lot more of is The ability to do configuration
Once, across multiple…
**Joshua MacDonald** 06:12 Yeah.
**Kent Quirk (he/him)** 06:13 Languages, applications, that kind of thing.
So it may be more effort to build that declarative configuration, but then you can reuse it, which is…
**Joshua MacDonald** 06:22 Yeah.
**Kent Quirk (he/him)** 06:22 a win.
**Joshua MacDonald** 06:23 Right, the OTel collector has a… implements that configuration. It's like V0.3 of the declarative config, and then you can
pass it that YAML block, and it will configure the Go SDK. I would love to be able to do that with a Rust SDK, even though I don't love the configuration struct.
**Kent Quirk (he/him)** 06:40 Yeah, but I mean, there's also a big push in JavaScript to do this, and Python to do this, so it's definitely happening. You know, we're seeing a standardization of the declarative config, so I think, I think you're right. I think there's value in thinking about what it would look like if we wanted to declaratively config samplers as well.
**Joshua MacDonald** 06:58 I guess I thought I'd mention that as far as, like, you know, when we talk about sampling, what… and what might be a good investment for us, or the group, or OpenTelemetry. I think that's probably where we're heading.
not really a call to action much more. I mean, I know, Peter, you had… you had mocked up something, and you had spoken to the configuration… declarative configuration SIG at least once.
**Peter Findeisen** 07:23 Yes.
**Joshua MacDonald** 07:26 I think there's a… I think there's a small amount of will to do that.
It'll grow.
Yep.
I don't have, I don't have a priority on it myself.
I also haven't checked in with any new… I haven't heard anything about the SDK sampler support. I filed tickets for Go and for Rust, and I haven't heard anything back, so I presume nothing's happened in Go and Rust. But as you can see, I keep talking about Rust.
I did have this prototype there, so eventually I'll probably push my prototype in, and then, you know, I know there's no declarative configuration support there yet, but…
That would be an interesting area to carve out.
Alright, you guys, I had nothing. I thought this would be a good time to see if we're… if we can have our time back, or…
I don't have an agenda, you guys.
**Kent Quirk (he/him)** 08:26 Sounds good.
**Joshua MacDonald** 08:27 Thanks for showing for a few minutes. It's nice to see you all. I really want to keep this meeting. Hopefully there's more to talk about next week. Next time.
**Kent Quirk (he/him)** 08:36 does it.
**Joshua MacDonald** 08:37 Thank you.
**Peter Findeisen** 08:37 Cheers.
**Otmar Ertl (Dynatrace)** 08:38 See ya, bye.
