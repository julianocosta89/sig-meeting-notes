SIG: SIG Injector
Date: 2026-06-11
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol** 01:55 Hi, folks.
**Jack Berg** 01:59 Hey, Bastion.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:01 Yay.
I just had one item I just wanted to bring up. There's a PR, from my colleague Matt.
Around, checkin.net.
Runtime compatibility version… Similarly to how we check the dependencies, because all .NETs are not supported by the SDK.
So, yeah, I think there's a comment from someone else on the .NET maintainers, but Matt, so there's a confusion about the… I just wanted to bring it up.
People haven't seen it.
Hmm… There was some change in the test that… I'm watching Costello won it.
Hmm… Alright, I think it's a missing commit or something.
**Bastian Krol** 03:54 Yeah, I've seen it, I did not really look into it, I'm not… really, don't really know too much about NordNet and the whole instrumentation there.
**But, I mean… It looks good, and I think you're already approved, right? So… Nikola Grcevski @ Grafana / OpenTelemetry** 04:15 Yeah, I just… yeah, I just wanted to bring it up. It's similar to what we both do for Python and, right? So we check for… Diversion, I think 3.9.
With the extra scripts.
**Bastian Krol** 04:31 Yeah, I think it's definitely… So, conceptually, what it says on the tin, I think it absolutely makes sense to have a check like this, if it can be checked.
externally, then… By all means, you should do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:47 Cool.
**Bastian Krol** 04:53 I guess this is a whole class of problems, to be honest, and I think some auto-instementation agents probably do something like that internally already, and… Maybe that's also… for some setups, the better place for it. So, for example, in Node.js, you could easily check the Node.js version in a pre-script and disable… Within the Node.js SDK then, and then that cannot be easily checked from the inductor, but it can be checked externally, and especially in some cases, it might be too late, I think in .NET, maybe you either attach a profile or don't, and that has consequences then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:36 Yeah.
**Bastian Krol** 05:37 So, that's… that's probably… Nikola Grcevski @ Grafana / OpenTelemetry 05:41 Good place to add it before we do that, right? Yeah, yeah.
**Bastian Krol** 05:45 Select it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:48 Okay, yeah, so I'll wait for Matt to address Martin's comments, and… They can merge.
**Jack Berg** 06:01 I was, looking at the agenda, and I thought that last week's agenda was this week's agenda, and I came across that issue about, setting hotel config file.
So I just responded to that. Does anybody understand this? This seems like a non-issue to me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:18 I don't understand it either. I tried hard to… understand what the question is. There seemed to be a problem I did mention, but…
**Jack Berg** 06:31 Anyways, I just responded and said, like, hey, look, we have this defaultENV.com file.
Any hotel underscore prefixed environment variable you specify in there will be, you know, injected into every process that matches your include-exclude criteria. And so, if you want to use declarative config, just set hotel config file in that.
And, you know, point it to your declarative config file, and… Thumbs up, so we'll see what they say.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:01 Yeah, you're right. I mean, I… I thought they would understand, maybe they looked into that.
But it seems to be some sort of, like, request not to have to maintain anything, but I don't understand how you don't maintain anything.
And you want a custom… Config file in a custom location that…
**Jack Berg** 07:28 Yeah, maybe… I don't know, let's just let them clarify.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:32 Yeah.
**Jack Berg** 07:34 I do find that… maybe this is related, but, like.
I find that our README is a bit, like, verbose, and, like, everything's sort of scattered around everywhere. I'm not sure when and who, but, like, I think at some point we should kind of do some housekeeping and just, like, you know, make a simple, terse.
README, and, you know, sort of organize all of our resources in a way that's more easily consumable.
Anyway, bye.
**Bastian Krol** 08:04 Yeah, I think I totally agree with that. I think the README doesn't really know whether it wants to be, like, more task-focused or a reference documentation, and then it's… not a good… doing a good job of either, so… yeah.
it's kind of… I guess that's just something that you need to do housekeeping on once in a while, because these things just grow with each PR, and each new feature or config variable added, and yeah.
**Jack Berg** 08:31 Yeah. Anyways, if I, if I open a PR at some point to do that, that was… that's kind of the motivation. I don't know if I'll have time, like, in, you know, immediately, but… Yeah. I'm thinking about it.
**Bastian Krol** 08:45 That's good, I guess.
I just added one more thing to the agenda, which… is the… so, I think it was Antoine, who opened the issue, and I think we discussed that in a previous meeting, that right now we only, allow, environment variables with this hotel underscore prefix.
And specifically, vendors.
using the injector might want to also add others, like Splunk underscore or something, right? That was a discussion we had.
And… I'm not sure… one… one person… Proposed a different solution than rebuilding with this weak symbol.
do we… do we have any opinion on that? To me, that sounds like a relatively big gun to solve that problem. I'm not sure. I didn't look into it too deeply, it sounded a… It could maybe be… a bit more fragile than we like, but I didn't really form an opinion on it. Did anybody… I think you also posted it in our Slack channel.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:08 But how's this different than the OTEL Java SDK, where you just have the OTEL environment variables?
to supply, I don't know, OTLP endpoint. You can't say Splunk OTLP endpoint, you must use the OTL exporter OTLP endpoint, right?
**Jack Berg** 10:24 They have a distribution of the hotel Java agent that has these Splunk environment variables, so I think probably what they're thinking is, like, they want to use the injector to inject their distribution of the hotel Java agent, and thus be able to configure the Splunk-specific environment variables that the distribution references.
**Bastian Krol** 10:45 I think the feature request is legit. I think the use cases for that are there, and I think should somehow be possible to support that. That's… not really what I'm… what I'm questioning. Of course, that… that can be debated, but I… but from my point of view, this is… this is a… legitimate future request, I'm… I'm specifically thinking about adding, adding this in honor… Or enabling this via a linker mechanism, if that is really… because we already do weird things with dynamic linking, so do we want to add this there?
**Jack Berg** 11:36 I'm not… I'm not really… opinionated about how to solve it. Like, so I guess, maybe we could talk through it, but the original proposal was, hey, we'll make it easy to provide an option where if you recompile the binary, you can customize the environment variable prefixes that we will ingest.
**Bastian Krol** 11:57 Yep.
**Jack Berg** 11:57 So, you know.
**Bastian Krol** 11:58 that produces on…
**Jack Berg** 11:59 No binary.
**Bastian Krol** 11:59 X. Yeah, yeah.
**Jack Berg** 12:01 Yeah, so, I… you know, one question I have about this alternative proposal, this dynamic linking thing, is, like, does that still require re… like, a different binary? For, like, Splunk to produce a different binary?
**Bastian Krol** 12:16 I think they could use the official injector binary and have a companion binary that adds this weak symbol, that's how I understand it. So they could use the binary that we built in our release process.
They still would have to provide, their own binary next to it.
And then also include that somehow… .
**Jack Berg** 12:44 Include somehow. Yeah, include somehow is, like, what I'm interested in, because, like, if it's just a matter of, like, putting this… this binary next to the injector binary, and it automatically detects it and picks it up, then that sort of negates the whole point of this security feature.
Right? So, like, if the injector is, like, looking in some place for other binaries to link to, and therefore, like, and those can influence the environment variables that will be injected, then an attacker can place their own binary in this location.
Adjust the environment variable prefixes that the injector will allow, and then use that as a way to manipulate the environment of every process on the machine.
**Bastian Krol** 13:30 Very good points.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:32 I agree.
**Jack Berg** 13:34 So I think, like, the tension is, like.
Anything that doesn't require rebuilding the binary sort of negates the point of the feature.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:46 Could they not just add their own LD preload before us, and then patch when they need to?
**Bastian Krol** 13:56 Sorry, they, they attach their own, they set their own LU preload, or.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:01 Preload something else as well, and then manipulate the investment.
**Bastian Krol** 14:06 So what was that something do that they… that they load before the injector? That would then monkey patch the injector? That… Nikola Grcevski @ Grafana / OpenTelemetry 14:15 I did a little fake one. Yeah, I guess. No.
I mean, just, translate the Splunk environment variables into the auto ones, and then… kind of, like, convert them, and then you re… we read the old ones, and then… But… Not if they want to set custom Splunk variables.
**Bastian Krol** 14:39 Wow.
From my point of view, the compiler, or the compile flag solution still sounds the most… straightforward, and I don't think it's… Too much to ask for someone having their own… for… Like, vendor that wants to use the injector technology to rebuild the binary.
That… that… doesn't… that's not rocket science.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:08 Yeah, that's the approach we use in OB.
So, for example, the versioning information that was… Put out in the traces, and… target info and all these places, they… you're allowed to override the vendor prefix of that, so you can say, this is Bela, it's not OB. That's Grafana distribution of this.
But that's a compile time thing, so you have to have a fork.
And override those variables, if you really want to go that path.
I like your proposal better, to have a compile time option that you can maybe choose your prefix, so if you don't want OTEL to be Splunk underscore.
**Bastian Krol** 15:53 Yeah, it wasn't my suggestion, I'm not sure who came up with it.
**Jack Berg** 15:57 I think that was Antoine's or Mikel's last week or the week before.
**Bastian Krol** 16:00 Yeah, yeah, yeah, yeah. Whatever, yeah, yeah, I think, okay, I respond there, and, and, asked for more… concrete information of how that secondary binary would come into play, because that is a good point. If an attacker can use that mechanism, then this is a no-go.
Good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:27 Yeah, if it's a companion binary, then I can put my own in there.
And unsuspecting, so maybe Splunk puts their companion binary, but if I know of this… Maybe I can put my own binary.
**Bastian Krol** 16:41 I mean, if you control LDP load, you can do anything, anyway, whatever you want, as an attacker, so that's… that's… Nikola Grcevski @ Grafana / OpenTelemetry 16:49 But it's maybe not as… yeah.
But LD preload, maybe I don't control, because that's LD preloaded yield injector, but then maybe I control where this binary sits, and then I can put this in, and then the injector will load it, unsuspecting.
**Bastian Krol** 17:04 Yes, yes, yes, exactly.
**Jack Berg** 17:10 Okay, so I think… none of the folks on this call are interested in injecting our vendors' environment variables, and so the folks that are engaging on that issue are Splunk and Elastic people, and so, like, we can steer the conversation and say, like, what is not going to work, but, you know, I think they are… They have to hash it out and drive the solution.
**Bastian Krol** 17:34 That's fair, yes. That's… that's fair.
**Jack Berg** 17:41 So I'm gonna leave a comment that just, like, you know, explains… because I don't see anybody talking about, like, why we are actually only restricting it to hotel underscore, and so I'm gonna describe that that's, like, a security feature, and, you know, share some of the context of this conversation.
**Bastian Krol** 17:58 Okay.
Thank you.
**Jack Berg** 18:05 That's all for the agenda. Should we… Nikola Grcevski @ Grafana / OpenTelemetry 18:08 Yeah.
**Jack Berg** 18:08 Did we drop early?
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:10 Yeah, I guess.
**Jack Berg** 18:12 That's great.
**Bastian Krol** 18:13 Sounds good to me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:14 Yep.
**Bastian Krol** 18:15 Okay.
Take care. See you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:18 Bye.
