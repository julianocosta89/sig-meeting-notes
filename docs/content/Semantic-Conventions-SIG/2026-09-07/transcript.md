SIG: Semantic Conventions SIG
Date: 2026-09-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi (Dash0 Inc.)** 02:38 Oh, hi, Jade.
**Jade Guiton** 02:41 Hello.
**Christophe Kamphaus** 03:32 Hello?
Let's see how many will join. Today is a US holiday.
Yeah, it doesn't look like anyone else will join. I would say, let's cancel today.
And next time, we will have the full hose.
**Michele Mancioppi (Dash0 Inc.)** 06:01 Well, not really, as far as I know, Ludmila's on vacation next week.
So…
**Christophe Kamphaus** 06:05 Oh, really?
**Michele Mancioppi (Dash0 Inc.)** 06:06 Why not be full house, but definitely there's going to be… Hopefully, there's going to be trust.
**Christophe Kamphaus** 06:12 Yeah.
And probably Church as well.
**Michele Mancioppi (Dash0 Inc.)** 06:19 Maybe, Christophe, you can, you can, Remind me, what is today, the process?
to expand… the, the enumerations for a cloud.platform.
**Christophe Kamphaus** 06:40 The enumerations for what?
**Michele Mancioppi (Dash0 Inc.)** 06:42 The cloud.platform, because we don't have Cloud SIG nowadays.
**Christophe Kamphaus** 06:46 Yeah.
I know that we discussed, the INUM values.
since… It's by default open.
We should not just add everything.
But only if it gives value to the semantic conventions. So if we have… Differentiations based on the values.
Then it makes sense to add additional Enium items.
So, if we would say, for a new cloud platform, we define additional metrics, of course it makes sense to then add, Add to Xenium items.
**Michele Mancioppi (Dash0 Inc.)** 07:31 I find we could have a more differentiated opinion for, cloud.
So, in general, that's the answer I remember as well, for cloud platforms.
I feel that for obvious services used across AWS Azure.
We should have one canonic way of doing it, because otherwise we end up with different things.
I'll bring it up next week, I can.
**Christophe Kamphaus** 07:54 I think for Azure and AWS, it makes sense to have it well-defined.
Since, we do have specific semantic conventions for those defined.
**Michele Mancioppi (Dash0 Inc.)** 08:08 Okay, thanks.
**Christophe Kamphaus** 08:10 Yep, see you next week.
**Michele Mancioppi (Dash0 Inc.)** 08:12 No, but if you want, you can leave. Jade, I think I have an answer for you, for the question you put in the agenda.
**Jade Guiton** 08:18 Oh.
Yeah, thank you.
Yeah, basically I'm… Doing some testing of some… basically of the Datadog SDKs, whether they fit the hotel Semantic Conventions.
and I found a few cases where some attributes that are normally resource attributes end up as fan attributes and vice versa, and I'm wondering if there's authoritative language.
**Michele Mancioppi (Dash0 Inc.)** 08:43 Let me get mobile, mobile and web monitoring spans.
**Jade Guiton** 08:47 No, just regular… regular… Regular spans in the tracer.
Problem is that Ditty dog tracers don't typically do this distinction, so…
**Michele Mancioppi (Dash0 Inc.)** 08:59 The, the answer that I recall on this topic is that technically, they're not bound.
To be at this specific level.
But, it is discouraged to be creative about where to put them.
**Jade Guiton** 09:18 Yeah, that makes sense.
The,
**Michele Mancioppi (Dash0 Inc.)** 09:20 So when you look at the Weaver model, you see affected attribute sets.
And it doesn't necessarily tell you where they have to go. But when you look at the Semantic Conventions.
there are things that are on the resource attributes.
Strongly implies they should be resource attributes.
There you see service, you see deployment, you see cloud, you see host, you see OS, and all the rest of the fun.
And, others, like, if they're not at resource level, they're effectively implied to be a signal level.
Because, literally, there is no semantic convention for, scope levels.
scope attributes. Like, I've never… Right. I've never seen a semantic convention for those.
And I… I'm sure Josh would have many more things to say on the matter.
But I think, effectively, if it's not specified in certainty Conventions, it's at least heavily implied that it should be let out.
**Jade Guiton** 10:28 Yeah, that makes sense to me.
It ultimately…
**Christophe Kamphaus** 10:32 It makes sense for efficiency in the protocol, because then you can group all the signals underneath the resource.
**Jade Guiton** 10:42 Yeah, yeah, you don't want to have to always look in two different places.
what I've been trying to do with Weaver is, The registry for each attribute group does give a type.
You have to type entity versus metric versus spam.
So I've been using that to try and kind of enforce that.
But I guess I'll have to be… I'll have to make it more of a warning than a strict violation of the spec text.
**Michele Mancioppi (Dash0 Inc.)** 11:12 This would also be if you do not want to wait until, the, Until next week, to get a more normative answer from the maintainers.
It would be both an excellent flyby question in the maintainer SIG tomorrow, or in the Semantic Convention tooling SIG.
Because today is vacations in the US, but the usual suspects, Mila Trask and jobs, they all congregate in the, in the tooling thing where they talk fever.
**Jade Guiton** 11:46 Yeah, that makes sense. I'm not really… I don't really need an answer, right off the get-go anyway, But I guess, yeah, it is good to know.
That, even if it's not strictly written in the spec, it is still heavily discouraged.
**Michele Mancioppi (Dash0 Inc.)** 12:04 Yeah, Christophev said something like, it's more efficient, to have the grouping for resources.
That is universally not true.
Because, for example, the… on mobile and web.
It will be actually more efficient for batching, To have a device.
and session.
To be a attribute level.
you end up creating a much larger amount of patches by splitting up by user and session and device ID and so on.
So, it's not, it's not really the rationale of what is more efficient, but it is what's more conceptually correct, in the light that Resource attributes are the ones that describe the system, where the data is coming from.
As opposed to any other consideration. At least that's a way of explaining to myself.
**Christophe Kamphaus** 12:55 Yeah, that's true.
And also, on the resource page.
In some conf, I put it in the chat.
There, the wording is really… it should be done like that, but you can also put it on the attributes of a signal.
**Michele Mancioppi (Dash0 Inc.)** 13:14 And by the way, nobody says that when you see, for example, ks.star in resource attributes, every single resource key in the ks.star namespace is a resource attribute.
Because, for example, there are metrics that I think were ratified by the Kubernetes SIG, where some of these things are used at the metric level, as opposed to through the resource. So it's, It's a bit murky, but in general, it seems to hold.
**Christophe Kamphaus** 13:46 Hmm.
I've also seen signals where it has been mixed up for technical reasons.
Yup, some…
**Michele Mancioppi (Dash0 Inc.)** 13:57 Okay, I hope it helps.
**Jade Guiton** 13:59 Yeah, thanks. That helps.
**Michele Mancioppi (Dash0 Inc.)** 14:03 then I would say, so, folks.
**Christophe Kamphaus** 14:06 See you next week!
**Michele Mancioppi (Dash0 Inc.)** 14:07 Right.
**Christophe Kamphaus** 14:08 Right.
