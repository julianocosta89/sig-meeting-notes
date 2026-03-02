SIG: GC Project Management (EU)
Date: 2025-08-11
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:26 Hey!
Good morning.
**Robert Pająk** 01:29 Hello, good morning.
**Pablo Baeyens** 01:32 How's it going?
**Robert Pająk** 01:34 It's fine, I'm in parent law.
Visiting?
north of Poland, so it's a little cooler, but it's very hot.
I don't imagine how hot is for… how is it hot for you, Pablo, right now?
**Pablo Baeyens** 01:50 Yeah, it's… it's improbable.
**Robert Pająk** 01:54 It's, like, 13 degrees, or what?
**Pablo Baeyens** 01:56 40-something today.
**Robert Pająk** 01:58 14?
**Pablo Baeyens** 02:01 Yeah, well… It's summaries like that.
**Robert Pająk** 02:05 Hey, dope.
Hey, Dan.
**Pablo Baeyens** 02:09 be done.
**Dan Gomez Blanco** 02:10 Oh, hello?
We're going up to, I think, 23 degrees here in Edinburgh this week, which is like, what?
**Pablo Baeyens** 02:29 I can share my screen if… Zoom alone.
Can you see my screen?
**Dan Gomez Blanco** 02:39 Yep.
**Pablo Baeyens** 02:41 Okay.
I mean, I don't think this is going to go…
Like, we're not going to start ignoring the resource on metrics, and I agree with Tyler that
I don't understand how that would help.
**Robert Pająk** 03:34 Yes, I agree.
**Pablo Baeyens** 03:37 Should we put community feedback, or…?
**Dan Gomez Blanco** 03:40 Yeah, I mean, there is one thing… there's… the only thing that I can think something like that could help is if you were to drop those attributes and use, like… depends on the backend, right? Normally, like.
Mmm… If your backend doesn't… You know, if you use, like, delta temporality, and your backend doesn't overwrite …
The… you know, when you send two data points for the same timestamp.
If it's sort of, like… You know, you can store, like, almost like duplicate data points.
Then it does work, as in, like, there are backends where that works.
I think, … not sure if InfluxDB does it, but, like…
yeah, InfluxDB or the New Relic, like, backend would also, like, be able to… you know, but still, you know, I think there is something in the, in the spec that says, you know.
That basically goes against this, exactly saying, like, you know, your resource attribute should be uniquely identified, and …
The metric, … Producer, so… I'm not entirely sure.
we can accept this? I'm not sure.
**Pablo Baeyens** 04:49 I guess we can… Way… To see if…
the conversation goes anywhere with Tyler and… the author… maybe… There's some other… change…
Probably in semantic conventions or something like that. That helps with the particular issue this person is having, so maybe closing it.
just… prevents the conversation from happening, and I wouldn't… I'll close it.
**Dan Gomez Blanco** 05:22 Yeah.
Also, like, you know, I guess….
**Robert Pająk** 05:28 But… … someone…
who doesn't want the resource matrix could just not set them, or is it not possible to just set empty at…
Resource attributes. I mean that I think that …
I don't think it's ever desirable, to be honest, to have it. I think that it is a food gun that later someone will see that one application has problems, and if everything will be under, you know, one resource, then they'll not be able to find out which… where is the problem, because basically every matrix will just, you know.
mixed together at the end. So, for instance, if you have CPU metrics or whatever, then what? You will have, you know.
for all the machines, so that's one thing that I think it's a bad idea, but secondly, I think if someone wants to have, basically, he just wants to have this behavior, he simply should just, you know, not use resources at all, because it means that, basically, you don't want them.
**Dan Gomez Blanco** 06:26 I think, … yeah, I think what they're saying here is that they… M…
I guess they use the same resource attributes for spans and metrics, right? And for tracing and metrics, and they…
You know.
And they want to keep them in the spans, but probably not in the metrics.
Also, like, there is a… there was a… thread under… Client side…
Let me see if I can find it… on Slack. Basically, someone was talking about, like, specifically adding a recommendation against using metrics and client size.
**Pablo Baeyens** 07:03 Yeah, I think that's what is being mentioned here.
**Dan Gomez Blanco** 07:09 Yeah.
I mean, because normally client-side doesn't…
Makes sense to use metrics, but…
There's nothing, normally nothing, not a lot to aggregate, right?
**Pablo Baeyens** 07:40 Yeah, I think this is the… Do you ship?
**Dan Gomez Blanco** 07:44 Yeah.
Is it worth linking that, I guess?
**Pablo Baeyens** 07:55 Yeah.
**Dan Gomez Blanco** 07:55 and say… Whoa.
**Pablo Baeyens** 07:59 Terrible.
Dude, …
So…
Should we just put deciding community feedback and let it… Continue? I mean…
I agree with Robert that this doesn't seem like a good idea, but I… Yeah.
**Robert Pająk** 08:44 I see it's for… Client applications. It's for web applications.
So, I just think it's any… yeah, I'm just writing a response in the background, so if everything… anything will be…
misleading, which I say it will be on me. But I think it's… they can simply create the resource for this kind of applications on their own, instead of using, you know, the default, the default resource, factory, whatever.
**Dan Gomez Blanco** 09:11 For the metric, yeah.
**Robert Pająk** 09:13 Yeah.
**Dan Gomez Blanco** 09:14 Metric SDK, yeah.
**Pablo Baeyens** 09:16 Okay, so I'm just going to do the community feedback then, and I'll let you, Robert, write the… Bing.
… Alright.
Yay.
I guess the dumb question I have with this is.
Why isn't it an alternative approach to just use… metrics, instead of… Spanish fruits?
Do either of you understand why?
**Dan Gomez Blanco** 11:38 Hmm…
So these are specific, I mean.
I just don't understand… Isn't the whole point of span events, like… This specific use case.
You know, like, individual… Blake.
Events within the scope of a span.
**Pablo Baeyens** 12:51 Yeah, but I…
I guess there's a more general question on, like, if you are not representing, like, an event in time.
Still, you need units, like HTTP request body size, and that doesn't have units. I guess…
Here, it makes sense that it's not a metric.
**Dan Gomez Blanco** 13:10 Oh, yeah, I see what you mean, yeah
Can you scroll down a little bit?
**Pablo Baeyens** 14:08 I also don't understand this.
**Dan Gomez Blanco** 14:16 I guess what they mean is that at the moment, well… the… So, like… deprecating… span events.
means that, I guess, for some…
Depends on the backend you use.
Would be more difficult to… Correlate logs to spans.
Okay, maybe that's what they mean.
As in, like, log event… log… logs that would be the, sort of, like, the future for span events that have, like, you know, trace ID, span ID, and then some type of, like… Yeah, yeah. They will be more difficult for them to handle, I guess?
**Pablo Baeyens** 14:57 Okay, I'm in my… My take here is that…
To bucket shoot that up to us, not… not us, adapt to the buckets, too.
**Dan Gomez Blanco** 15:05 Yeah, yeah.
**Pablo Baeyens** 15:05 And the things that we ask for them is reasonable.
**Dan Gomez Blanco** 15:09 Yeah. No, I think, you know, that's outside of the scope of discussing here. I mean, that was already discussed in the discussion to deprecate span events, right?
**Pablo Baeyens** 15:24 I… Don't have a… -
I think community feedback is probably… like, it's not clear what to do here, it's not as clear as before that this is, like, a…
Bad idea, at least to me.
….
**Dan Gomez Blanco** 15:44 As this is, like… is this more like semantic conventions?
Or should we….
**Pablo Baeyens** 15:52 The semantic conventions can only represent what the proto allows, and the proto does not allow it to specify.
**Dan Gomez Blanco** 15:58 Yeah.
**Pablo Baeyens** 15:59 units.
Were you going to say something, Robert?
**Robert Pająk** 16:07 No, no, I just think that it could be left here.
this issue.
**Pablo Baeyens** 16:16 Okay.
Speak back…
This is probably accepted without a sponsor, like, it's just… A clarification?
That needs to be done.
**Dan Gomez Blanco** 16:48 Yeah.
**Robert Pająk** 16:58 Don't have this kind of… Okay.
**Dan Gomez Blanco** 17:02 But needs a spon… need to sponsor, or… well, without not accept it.
**Robert Pająk** 17:06 She's confused.
**Pablo Baeyens** 17:07 if it….
**Robert Pająk** 17:08 I think it's gonna be just accepted, yeah.
**Dan Gomez Blanco** 17:11 Yeah.
Can we ask him… Man.
**Pablo Baeyens** 17:41 … Then we can look at the…
follow-up… did we add the follow-up to the filter? I can….
**Dan Gomez Blanco** 17:51 Yeah, I think that was added now, and if we're using the filter in….
**Pablo Baeyens** 17:56 Yep, okay.
So, that should be it, and I guess the update here is your comment, Robert? Yeah.
**Dan Gomez Blanco** 18:07 Man.
**Pablo Baeyens** 18:16 Okay.
So, I think we are… Dawn, then?
Or is there anything else that…
Do you want to look at….
**Dan Gomez Blanco** 18:25 No, I think that should be fine.
**Pablo Baeyens** 18:28 Okay. By the way, I left…
A couple of small comments on your… …
Is it on community, your PR, about project management?
**Dan Gomez Blanco** 18:39 Yeah, some draft still until, you know, I'll be working on the….
**Pablo Baeyens** 18:43 Okay, it's just, like… a Tyco one.
**Dan Gomez Blanco** 18:47 Cool. Yeah, I'll be working on the scripts for this this week, … But…
Yeah, I think, you know, … Austin pushed the scripts for… that he used for…
the… basically to extract the information using, like, OpenAI from… from the… the… Project proposals.
I'm planning to make that a little bit less… AI-driven, and more.
attribute-driven, or, like, process-driven, basically, I guess.
So that would… yeah. It's just gonna be more based on the… segs that,
take on projects, basically, I think.
either new SIGs or existing segs. But yeah, so, anyway, I'll discuss it on Wednesday as well, and the GC meme, but…
I'll trade two bits.
Cool. Awesome.
**Pablo Baeyens** 19:45 Alright, see you next week.
**Dan Gomez Blanco** 19:49 See ya, bye-bye.
**Robert Pająk** 19:51 Thanks, bye.
