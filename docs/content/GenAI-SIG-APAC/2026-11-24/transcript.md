SIG: GenAI SIG (APAC)
Date: 2026-11-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:20 Hi, Liudmina.
**Liudmila Molkova** 01:23 Hi, Steve!
How are you?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:26 I'm good.
How about… how about you?
**Liudmila Molkova** 01:31 Good, thank you.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:32 Yep.
I, I found, yeah, last week, the committee released the first version.
In the mute.
GenAI repository, and yeah, I think it's very… it is very good.
**Liudmila Molkova** 01:48 Awesome.
Did you depend on the release in some way?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:54 I'm sorry?
**Liudmila Molkova** 01:56 like, how does the release affect you? How do you… I think it's useful for you.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:03 Yeah, I, I think, I, I asked this question, last week with Trask, and we want to have, release, because, our instrumentation wants you, follow the, latest, GenAI semantic convention, but without, release, we don't know how to, update our, implementation.
**Liudmila Molkova** 02:31 I see. Okay.
It makes sense.
Yeah, I don't know if Trask is joining.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:46 Yeah.
**Liudmila Molkova** 02:47 Cindy added the cost to the agenda.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:51 Yeah, yeah.
**Liudmila Molkova** 02:55 So do you… What do you want to discuss it?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 03:02 I found that in current semantic convention, we define some attribute to capture the token usage.
But, in, some, coding agent, or related SDK, they will, yeah, use, another, another way to, calculate, token usage or a cluster for user, like a KrieD, or something like that. And, yeah, I want to know whether we, do we need to define some, attributes or, adjusted the token usage attribute to, To meet the requirement in a scenario like a credit.
**Liudmila Molkova** 04:07 Yeah, so the, the, the trick is that like… Instrumentations don't know what the cost is.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 04:16 Yeah, but, yeah, maybe in some SDK, such as, I'm not sure, Cloud Code SDK, whether it provide, related credit for, instrumentation, but in some, SDK, I, I've… I heard from my colleague, he said in Coder SDK, it provides a pretty, usage.
So, in that scenario, so maybe they can get the, credit, correctly, and, capture related, Attribute to the instrumentation.
**Liudmila Molkova** 04:58 Yeah, like, the… in a common case, The pricing is not… It's known to the instrumentation, because it's individual per, like… Customers, right?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:15 Hmm.
**Liudmila Molkova** 05:16 And… It's just that… It should be some additional component that knows About the pricing information specific to this customer.
That can report these metrics.
And… But… it's super useful, I… I don't doubt. It's just… what is… what an OpenTelemetry ecosystem Would know that maybe a collector processor.
Or, yeah, some manual instrumentation. Then do we… Need to define something here, unless we have some generic story.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:02 Okay, yeah, you mean, yeah, you mean it's, useful, and, if, we have, specific, Yeah, evidence or, stories, maybe we can… Do something in these scenarios.
**Liudmila Molkova** 06:20 Yeah, like, if we know how to… Vlad customers, or… Something, configure the costs.
Then we could report these things.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:38 Okay, okay, makes sense.
And, another, another thing that I want to discuss is about the, user ID.
Yeah, yeah, this, I, I… I sent a PR, before the KuberCom North America, and, I'm not sure, yeah, do, are you interested to discard the, Content again.
I, I can send a PR story.
**Liudmila Molkova** 07:14 Yeah, I, I think I remember it, and what we, I think what we ended up with is Probably it should be somehow scoped to GenAI, but then it's still not super clear what it is. And that essentially
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 07:32 Yeah, I added the link to the agenda.
**Liudmila Molkova** 07:51 Yeah. Aww.
Remember this one.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 07:55 Hmm.
Yeah, currently, yeah, follow up the, previous discussion, I, I think, yeah, maybe, GenI user ID is, yeah, it's a better.
option, then the user ID.
Mmm…
**Liudmila Molkova** 08:29 Yeah, do you want to emit it for, like, in your instrumentations for all SDKs, or… Or, let's say, your SDKs only.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 08:38 in fact, in our, in, implementation, yeah, we defined, attribute called the GenAI user ID, and, we will, capture this, attribute, yeah, from some, from some, framework, like, Agent Scope, or something like that, in our, in our, implementation.
**Liudmila Molkova** 09:10 Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:13 So, You sent this, content to Auto GenAI cementing Convention.
**Liudmila Molkova** 09:23 Yeah, I see. I mean, it makes sense.
And, like, with GenAI.
It is… scoped enough.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:39 Yeah, maybe, I think if you think, it will, cause conflict with other concepts, like, user ID in semantic convention hotel, maybe we can clarify the scope and, to, to describe, yeah, maybe, like, GenAIU's ID is, not represent something like the, user ID from browser, or something like that, and we clarified the scope of these, attributes in, Autel GenIM Convention, and, let the user know, how to capture this, attributes, and, What is the means of these attributes?
**Liudmila Molkova** 10:30 Yeah, like, if we say that it's the… the user information provided by the framework, the Agentic framework, for example, and we give A couple of examples.
And I think that… That's reasonable. Like, currently, it's still the user.id.
And I think you have a comment where you're suggesting to switch to GenAI user ID.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:57 Hmm.
Yeah.
**Liudmila Molkova** 11:00 So, like, if you want to update PR to the GenAI user ID, then I can review the, Don't even mention the user ID, like… Like, if we describe what it is, that this is whatever is provided in the framework.
Then we don't need to mention the browser thing.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:28 Hmm. Yeah.
**Liudmila Molkova** 11:30 And then, Yeah, let's… I would be happy to review and maybe suggest some other tweaks, but eventually prove it.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:39 Yeah, okay, thank you.
Yeah, I can, do it later.
**Liudmila Molkova** 11:45 Okay.
Sounds good.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:52 Okay, yeah, I don't have more content to discard today.
Yeah, thank you, Ludmila.
**Liudmila Molkova** 12:00 Yeah, thank you. Have a good day.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:03 Yeah, have a good day.
**Liudmila Molkova** 12:05 Thanks, bye.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:07 Bye.
