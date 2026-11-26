SIG: Collector SIG (EU/ET)
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 06:53 I guess we can get started.
Is there anything for… high priority issues?
And I think I have… Couple of PRs?
the… maybe I can mention here, so… let me… Copy those. There's… two PRs… Or removing deprecated components on… The chord is true.
And then… I have the PR to… mark the OGLP receiver as B1.
Which is… This is lost.
Like, I… I added all the links to the meeting notes. I will keep those open until… At least next week, cause… because of Thanksgiving, there's, free people that are out.
But… Yeah, otherwise, feel free to… Trivia?
And if there's no other… High priority issues, things, We can move on to the telemetry resource leaks thing.
**Mikołaj Świątek** 08:45 Yeah.
I don't think I really need any decisions, I just wanted to point it out, and I just filed them, like… half an hour ago, so if you haven't seen them, that's not really surprising. But basically, there's… there's actually… I found them for metrics and logs, because these I can easily reproduce. It does actually also exist for traces, although it's a little bit harder to… trigger, because of the, the tracer is a little bit lazier about when it instantiates things.
But basically, both… all of these have the same shape, essentially, and that is when you create, like, a logger, or a… or you pass a meter provider into a component.
And you set any kind of scope attribute, which, for loggers, we do unconditionally. For meter providers, we do if the new pipeline telemetry feature gate is enabled.
What happens is that the SDK internally caches, Some things?
And it's in par… and we don't, drop those caches.
So… and, right, if you don't also… if you're not doing partial config reload, it doesn't matter, because the reload recreates the service, and so it creates all the telemetry providers, so everything gets dropped because of that.
But if you're doing partial config reload, you're essentially leaking some stuff per each component that you create, and the component gets deleted. Those… telemetry resources don't get deleted. If it's… in the case of a logger, it's, like, 500 bytes of a ZAP logger. In the case of metrics, it's more stuff, because there's, like, readers and aggregators and other bits inside the SDK that also gets cached.
And this only really happens if you start setting scope attributes for, like, reasons that I assume are, like.
I assume there are reasons for that, I don't know the SDK, to go SDK that well, but essentially, like, this is a… a leak that happens. And… I think fixing it for logs is very straightforward and simple. Fixing it for metrics is unfortunately not so straightforward, because there is no way to actually release the resources that the meter provider creates. It's, like, there's, like, a cache in there that includes the scope attributes, and… there's no way. You can unregister a callback on an instrument, but you can't actually drop that. And so, there is actually a way to fix it, and in the issue, like.
in… because in Elastic Agent, we actually enable the… or in our… in our auto Collector distributions, we enable the partial config reload flag. So we did fix it, but fixing it required a bunch of, like.
More complex than you would expect manipulation of the, like, having a meter provider that's secretly, like.
gives you a meter provider every time you ask for a meter, and then tracks the life cycle, and so on. It's a bunch of work to do that, and the reason is, again, that the SDK doesn't actually let you, and it's a little bit related to the spec.
Question… long-standing spec question about, Being able to drop instruments.
As well. I see there's, like, a pull request from David Ashball.
about that. I'm not actually sure if that would help fix this, but it's, like, roughly the same problem.
But yeah, if anyone wants to discuss or have questions or anything, I'm available. I thought about this problem a little bit. Other than that, it can just be handled asynchronously.
**Jade Guiton** 12:44 I guess one question from me would be… Like, is there something we can do on the Collector side to… mitigate this… Where is this… really something we have to wait on the Go SDK for first.
**Mikołaj Świątek** 13:01 It's possible to mitigate both of all of these in the Collector. How complicated doing that is, and how… how much you have to kind of… work around the SDK to do it varies. I think the logger one is very simple, and we can do it. The metric one is more complex and requires workarounds. You can actually, like, if you go into the issue, you can actually see how the workaround for metrics actually looks, and what it does. It's like… actually, the one we have is more complicated, even, because it can't… it has to kind of reproduce what, what the auto Collector itself does, like, it replaces certain bits of the telemetry instantiation logic.
For traces, I honestly have not checked.
It's kind of a question from metrics, I think, whether we want to see if… if the SDK will help us out, like… Relatively quickly with this, or… and if not, then we can think about doing some tricks with the meter providers.
Of our own.
**Jade Guiton** 14:13 Okay, got it.
I'll look at the issue and… I'm interested to… Let's see what that looks like, because it could potentially be… I mean, I don't know if it would need to be a blocker, but it would be something we might want to resolve before we meet the feature gate beta.
**Mikołaj Świątek** 14:31 The new pipeline telemetry one, right? Yeah, I agree. Yes.
Alright, that's all I have. Thank you.
Igor, you're next. You're here.
**Igor Peschinskii** 14:47 Yeah, thanks.
I don't know if PostgreSQL receiver maintainers are in the school, but… I just wanted to briefly mention that I created an issue, to… Like… We want PostgreSQL receiver to emit the metadata about table schemas and… indexes, and… Primary keys and that kind of stuff.
This would require creating a new scrapper, All the information required, can be taken from the Postgres system catalog without any additional permissions. So, I described it in this issue, like, the The attributes of the event that we want to emit.
So, yeah, all the details in the issue, if anyone have some opinion or suggestions, I would be happy to hear.
**Pablo Baeyens** 16:11 Yeah, I… I don't think there's anybody who is a co-owner of this component right now on the call.
I guess if somebody knows slash works with somebody who is a code owner here, Could be.
Good, too.
Let them know.
**Igor Peschinskii** 16:39 Yeah, if there is no other comments.
I think we can move on to the next.
Sure.
**Pablo Baeyens** 17:02 I think that would be… You'd be Bonsai?
**Vibhanshu Singh** 17:06 Yeah, hello, everyone.
I'm Vibhanshu, I'm… Currently a Collector Contract writer.
So, this is my first time… Talking with you all in the SIG.
I'm a bit nervous right now.
I have a PR to review. It's been up for a while now.
Let me paste it in the chat.
This one, I believe.
So, it's about removing the feature gates, stable feature gates.
Which was scheduled for the version… 0.166.0, but… The contract version got released yesterday, so I think it… elapsed that time, so I would really appreciate a review on this.
**Pablo Baeyens** 18:10 Yeah, this looks reasonable to me.
**Vibhanshu Singh** 18:15 Yep.
**Pablo Baeyens** 18:16 Oh… I'll review after this call.
Okay.
**Vibhanshu Singh** 18:23 And one more thing, I and Dimitri are basically working on the new metric model.
Which he proposed, I believe, in May this year.
So, I have read the meeting notes, which happen in person in… during the KubeCon, and I have seen that, period, In the core repositories, Well, going to be unmaintained, so I would like to help there.
As an additional code owner.
Along with an active approver or maintainer with me.
I would really appreciate that.
**Pablo Baeyens** 19:00 feel free to file a PR, for getting to be a code owner. If you can… Like, listings you've reviewed on that particular area, that would be… Great, if you haven't…
**Vibhanshu Singh** 19:15 That's… that's great, that's great.
Thank you.
**Pablo Baeyens** 19:20 Thanks.
I think that's… all. Anything else?
All right, then… thank you, everybody.
**Evan Bradley** 19:56 Bye, everyone.
**Pablo Baeyens** 19:57 See ya.
**Vibhanshu Singh** 19:58 Okay, everyone.
**Jan Korona** 19:59 Thank you, I…
