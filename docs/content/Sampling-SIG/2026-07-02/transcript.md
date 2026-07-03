SIG: Sampling SIG
Date: 2026-07-02
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 06:34 Wow, look at all these people.
So, aiming at, mic?
**Mike Goldsmith** 06:40 Hello, good morning.
**jmacdonald** 06:42 And, one new face, or one new name, hello. Let me pull up our notes. Sometimes we are there for our meetings. I see an agenda.
And, maybe we'll say hello to, the… new person, Ian, welcome.
**Yingrong Zhao** 07:07 Oh, my name is Ying Rong.
**jmacdonald** 07:09 wrong.
**Yingrong Zhao** 07:10 Thank you.
**jmacdonald** 07:11 Hi, pleased to meet you. We have, on the meeting notes, meeting agenda, meeting invite, some notes. I'm gonna put some notes here.
And Carlos has given us at least one thing to review, and Mike, I know you have a large PR, maybe we could ask you to talk about that a little bit.
Yup.
Well, I know this PR. I have reviewed it. Looks like we have 3 approvals.
And Carlos put it in the agenda to discuss. Do we feel that we need any more, Attention on this, Peter?
**Peter Findeisen** 07:56 Well, I'm… I'm fine with this. I thank you for your… for your approval, and… Yeah.
**jmacdonald** 08:03 Very good. Yeah, I… it was… I mean, I'm very technical, of course, but I, both believe it and trust you. That's two things.
So, yeah, just minor adjustments here. I think we can tell Carlos that these are, that this is good to go.
Hit.
Does remind me of my, misgiving. I wish that I could push people faster, at least my own people, to push forward on Rust and .NET for those composable samplers, and I am.
I was going to reflect on that for you all. We have such a problem with logs… logs volume right now.
that no one is paying attention to sampling traces. So that's at least a topic that we could maybe riff on.
So, I'm gonna write here that this looks good.
Beautiful.
**Mike Goldsmith** 09:00 use the log dedupe processor in the collector?
**jmacdonald** 09:04 This is, a sort of, like.
internal story within Microsoft where we're not using the collector at all. It's more of a legacy story.
I… I… good to hear about YouTube. I'm aware that it's there. Do you, recommend it?
**Mike Goldsmith** 09:25 I do, so I, I introduce both the log dedupe and the, the log, the drain temp, the drain processor, and if you combine both the drain processor and the log dedupe together, and then get the log dedupe to dedupe on the template that's generated, you get huge reduction in, log volume.
**jmacdonald** 09:46 Let me… let me write that down, because I think I understood what you said, but maybe for the room.
So, logs is a new alg… it's a drain is an algorithm.
**Mike Goldsmith** 09:59 That's right, yes. Drain is an algorithm, so there's a new process, a contrab processor, in… Yeah, contrab processor, it's been around for a couple of releases now, that uses the drain algorithm to look at logs logs bodies, take the string, and then generate a template from them, so anything that's consistent will be able to remain. Anything that varies between… after seeing multiple iterations, it'll replace it with a placeholder.
That template is then attached to the log to say, this is the template that this looks like. So, like, IP addresses or usernames or other things that are very… that change frequently will get… will be basically anonymized out of the template.
That will… and then the processor adds the template to the log. You can then do something else with that template further into your pipeline, or in your backend, or whatever you want to do.
Such as to use the transform processor to drop them, or use the filter processor to drop them if it's something it doesn't want, or the log dedupe processor, which given a set of attributes, it will then try, and over a period of window, it will then keep one, add a count to that record, and then only send one on in place of X. So these two things together work together really, really well.
**jmacdonald** 11:12 Cool.
Good to hear. Yeah, I, I saw you do all those things, but it's nice to be reminded, of, of the practice.
I remember I knew something like the drain algorithm very long ago, and it… Got it closed, but working, so I'm glad to hear that this one does.
**Mike Goldsmith** 11:31 Yes.
**jmacdonald** 11:33 Yeah, well, naturally, before we move on from that, naturally, I end up asking or thinking about whether I'm getting logged to metrics accurately or unbiasedly, and it, Reminds me of at least the vision to be able to count things that you sample, and, seems like The… the… what's on my mind, at least, is how, when we sample traces, we talk about consistent probability sampling, and when we sample logs, although there is a nice story you can make up or tell about consistent probability sampling in logs, it isn't always the case that that will work. You either don't have your tracing identifiers, or you… Or what? I always find myself looking at non-consistent sampling, you know, just like reservoir sampling in general to try and put hard limits on logs, but that's really maybe off-topic here, or at least out of focus.
Okay, so I'm done talking about that one. Any comments or thoughts on… My, my tangent.
Doesn't have to be. So, Mike, let's talk about, dynamic sampling, the work that you've been doing. Maybe give us a quick overview. I'm easy to get approvals from in sampling, by the way. I think everyone should know that. But, I've followed enough to know Honeycomb over the years that you have some good technology. So, maybe you want to talk about it?
**Mike Goldsmith** 13:16 Yeah, of course. Ingrong's also probably a good person to speak about this as well, but I can give an overview, and then we'll… then they can add in afterwards as well. So, Honeycomb has a proprietary tool called Refinery. We've operated that for many, many years.
That is a tool that is a dynamic sampling, proxy, so it lives outside of the collector pipeline. It's owned and operated by… Honeycomb. It is also open source. And what that does is it introduces dynamic sampling algorithms rather than probability-based ones.
So it's got similarities to what the till sample can do, so over a period of time, you then define some rules that you want to apply over that, and then apply, and then take a portion of that based on certain rules or policies that you define.
So in refinery, the refinery, product is organized around, Standing up an instance, and then defining rules, and like, making sure that your rule… that you've got an endpoint to send rules to, and then it depends on an external library called the Dyne Sampler Go, and that is where the actual algorithms live, and that exists as an Apache 2 open source library that anybody could come and use if they so wish to.
So the focus of this work, which is both the issue and then the supporting POC, is to introduce that library into the collector so those sampling algorithms are exposed and usable by somebody in the collector instead of using Refinery, which is a proprietary tool.
There's a few different types of algorithms there. There's a windowed one, there's a throughput, there's a… I think there's another… I think there's four.
So yeah, that's the goal, ultimately, is to try and introduce those dynamic sampling algorithms to the collector as a separate processor. I've talked to both Josh and to Chris, and sort of explained through why the dynamic sampler implementation is different to what we currently have in the tail sampler, and some of the conflicts of how they're organized and how they work with each other, so that's why we've decided to go with a different processor.
Yeah, I think that's a general overview. Ingrong, do you have anything to add?
**Yingrong Zhao** 15:27 No, I think that's a good overview. Thank you.
**Chris Marchbanks** 15:31 Like, the biggest difference is, like.
really, like, it's less that the dynamic sampling exists, it's like, you… we could get dynamic sampling into the tail sampler as well, and… it exists in, like, we've done that in Grafana Cloud, it's just on the proprietary side, which is kind of frustrating to me.
But, like, the big difference is this trace state handling, which… and have a, like, that's the big difference between these two processors, is I have a list of first rule, and then I never drop through, versus this.
big ore of policies. Right. That's the real difference between these two processors.
**Mike Goldsmith** 16:13 Yeah, so I… so yeah, after… with some, when Chris and I were chatting, we did find the, tail sampler does have a… was it the… what's… I can't remember, was it? Sample on first match property, which allows it to say, I'm going to work through the list of policies, but unfortunately, all of the implementations of every policy, then ex… if you get a no result from… the policy, it then falls through to the next one, where a dynamic sampler is configured to say, if I tell you a no result, that means I've given you the decision to drop it, so it's a very different dynamic there.
**jmacdonald** 16:51 This… this gets toward… to my, sort of.
feeling of confusion sometimes when I think about the tail sampler processor.
Can I ask, when we, just, just, this is maybe… maybe an easy question, but when we insert the OTTH threshold value.
What I'm assuming you're doing is taking the output of your rate calculation, or your dynamic decision making, Translating that into a probability number, translating that into a threshold, comparing against the trace randomness, to achieve compatible, adjusted counts and behavior with the threshold values.
**Mike Goldsmith** 17:35 That's right.
**jmacdonald** 17:35 That's what I would expect, but I just wanted to check with that.
Yeah.
**Mike Goldsmith** 17:39 That's right, so in here… so in the PLC, and then in the… there's a tracking issue linked to it as well, so this is just setting outbound thresholds, but it does both the inbound… I would like to add the inbound as well, so if a head sampling decision has already been applied, it can then calculate based off that value rather than a non… a no value being provided, and both input and output are based on the package sampling calculations.
Very good. So the algorithm will generate a sample, and then it will then convert it to a threshold.
**jmacdonald** 18:11 So then it acts like the equalizing, Mode of one of the basic samplers that we have.
In terms that I've used in the past. Cool.
Well, I think this is healthy. I think there's… it's okay to have, like, overlap and multiple solutions at this stage of the game for us, and so I… I see this as, a great step forward. So, thank you, Mike.
**Chris Marchbanks** 18:38 Yeah, I do have one question.
**Mike Goldsmith** 18:39 Thank you.
**Chris Marchbanks** 18:40 How open is… how open is Honeycomb to, like, contributions to DIN sampler? The, like, the… the algorithm, the underlying algorithms? Is that…
**Mike Goldsmith** 18:47 Perfectly open. Okay, cool. No one has ever… I think we may have had some external contributions to it in the past, but typically people focus on Refinery rather than the library that it's built upon. But yeah, it's an open source Apache 2 project. If you want to create… if you want to make a suggestion, please do so.
**Chris Marchbanks** 19:05 Cool, yeah, like, I've tried it a little bit, like… I think we discussed, I've ran into, like, oversampling problems with it when I've tried it in the past, like…
**Mike Goldsmith** 19:14 Yeah.
**Chris Marchbanks** 19:14 I just wanted to make sure, like, if people run into this in OTEL, we are happy to go and, like, change how it works a little bit. Or… yeah. Great. Sounds good.
**Yingrong Zhao** 19:23 Yeah, I think the window throughput sampler is contributed by an external, external source.
**Chris Marchbanks** 19:32 cool.
**jmacdonald** 19:34 So these will all be essentially, rate adjustment mechanisms that will have pros and cons, I guess, like, you know, variance or, you know, behavioral issues, dampage, you know, like, slow response or fast response and so on.
**Chris Marchbanks** 19:47 Yeah, those decisions around, like, what to do when you see a new thing that is… that, that can be…
**jmacdonald** 19:56 Yep.
**Chris Marchbanks** 19:56 Yeah, you have trade-offs, basically. Do you want to sample more stuff, or do you want to save on cost? And it depends on the…
**Mike Goldsmith** 20:05 And then how long do you remember something for, and if there's multiple windows to that, because if your windows are short, but you might see something come through infrequently, and how it adjusts for that, because you don't… maybe you… it's really bursty, and then it might miss windows, and that can then, or as you say, over… overpopulate a sample.
**Chris Marchbanks** 20:22 Yep.
**Mike Goldsmith** 20:24 Yingrong and I have dealt with those questions on a number of occasions while dealing with refinery, so there are ways around it, but yes, contributions to this report, and then we'll have to make sure that those options and the way that you configure are well-surfaced inside the processor, too.
**jmacdonald** 20:42 Cool, it's also nice to see that this has just been, you know, production tested and, like.
For some years, so that we can… you know, get through the sort of rough patches of untested sampling algorithms, which I've seen enough of.
**Mike Goldsmith** 20:58 Yeah, we use… we've used it in Refinery for 7 years now, so it's… it's well used.
**jmacdonald** 21:06 Very good. Well, I think I've already given an approval on this, but, just to be clear, I approve, and Thank you for this, Mike. I'm glad to see. I mean, so… so is refinery still, is refinery still a thing, or are we moving pieces of refinery into OpenTelemetry Collector? Maybe that's not a question you want to answer.
**Mike Goldsmith** 21:33 Yeah, no, I can answer that. I think, structurally, they have different goals in mind, so the collector has a very different deployment pattern to what refinery is. Refinery relies on a gossiping pattern between instances, where the collector just isn't set up to do that.
I would like to, outside of, like, the initial milestone that we've set up in the issue, I would like to explore more of, like, the storage-based extensions to see if we could make, multiple instances than share state, or deal with that in a better way. I think, ultimately, I would like to see refinery deprecated in place of the collector, and that'd be the preferred pattern. But I don't know how long it'll take us to get there, and operationally, if it will ever be identical to what refinery is. So I think it'll be a very long tail, but possible.
**jmacdonald** 22:20 Yeah, that makes sense to me. I'm, drawing connections, at least with my… I'm aware of what a large-scale metrics ingest pipeline looks like, and you sort of need to do some management of the same nature. Like, you can't… you have to load balance your work in a certain way, and that's one thing you're doing with gossip.
You know, not quite the same, but… as the collector hopes to grow into more uses, I think the ability for it to… shuffle and load balance and partitions data is really what's key, and that's what Refinery has right now.
**Mike Goldsmith** 23:02 That's right. That's definitely the biggest thing, and I think the exploration when we get to it, I know that there's been some work with, like, the PebbleDB extension to make the individual instances memory, like, footprint a bit smaller by using a disk cache.
I would definitely like to explore… whatever exploration we do for the possible sharing of state, I think would be applicable to not only the dynamic sample, but other samplers as well.
So, hopefully it'll be everywhere.
**jmacdonald** 23:33 Did you see, this conversation, in the past? I think you probably did, that the folks at Victoria Metrics have moved into the tracing space a bit, and.
**Mike Goldsmith** 23:44 Yes.
**jmacdonald** 23:45 proposed something called retroactive sampling, and, I went to watch the talk so I could check out their blog post, which, didn't… wasn't a fit for the OpenTelemetry blog at the moment, but, it contained a nice idea, and it sounds connected with what you're looking for, or at. Mainly just that, performing, sort of, key-value storage, like PebbleDB supports, gives you the impression that you can just randomly access your storage when you're writing traces, and it performs very poorly, and so the main system architectural point in that talk was to put your trace data into a FIFO storage, defer your sampling decision for a period… fixed period of time, and then at the end of that period, start dequeuing from your FIFO. You'll have your decision at that point, and it'll be sort of linear storage access.
I was encouraging them to, like, get involved. If they do, that would be great. If they don't, there's still an idea there that I think enough people might want to think about. I, I mean, large-scale ingest is, is typically not something you find strong solutions for in open source. You know, that's kind of like what vendors are competing on, so, So, there's… for me, there's a question of, like, it's an odd duck to find a large-scale, single-node collector that's, like, storing its own data, but not involved in a system or a cluster to do load balance. So, I'm… I'm open to it, and I'm watching, and I'm trying to help, but I… I don't quite see where it's going.
I'm sure there's a category of users for which this is fine, and, but maybe not for all scales.
**Mike Goldsmith** 25:29 Yeah.
Yeah, I agree. I think it's definitely got challenges built into it about, especially when you go to really big scales, when you've got, like, 100 collector instances all communicating, or trying to do random access across a number of shared state. Wherever that state is stored, it's going to be difficult to manage and coordinate across.
Yeah, I'd like to… I think we're very interested in seeing how that could work with the collector, because it has got such a different deployment pattern to what Refinery has.
I think the ultimate goal would be, even if it's not as… perfect. I think getting away from, like, the two deployment pattern that we have to advocate if you want more than one big instance is, is challenging for a lot of people right now.
**jmacdonald** 26:15 Cool. Well, we've spoken about it. I… I'm glad to see it, let me know how I can help.
Aside from approving things, of course.
We've reached the end of our agenda. I figure the best thing we can do is not hold the meeting on longer than it needs to be. Did anybody else have, Things they want to talk about.
**Chris Marchbanks** 26:40 did have one. How can we get the Go consistent sampling PR merged?
**jmacdonald** 26:45 Oh. Hasn't merged yet?
**Chris Marchbanks** 26:47 It has not merged yet. It's been, like.
two… a month or two? It's been approved for at least a month.
**jmacdonald** 26:53 Yeah.
**Chris Marchbanks** 26:54 pinged multiple people.
**jmacdonald** 26:56 She would be out today, she couldn't make it to the meeting, so I guess I can try to push on that for her.
**Chris Marchbanks** 27:02 Yeah.
**jmacdonald** 27:02 Josh will press on this.
**Chris Marchbanks** 27:08 Thank you.
**jmacdonald** 27:10 Easy.
**Mike Goldsmith** 27:10 I know a few people in the Go SDK place as well, so if you'd like, I can try and reach out, see if someone, or press.
**jmacdonald** 27:16 Yeah, Mike, if you don't mind, if you… if you have anyone with approver or maintainer powers, I can't think who you might have, but I'm sure you might. So, yeah, anyone with a vendor connection to a no-tel Go person, that could help. But I can also…
**Mike Goldsmith** 27:30 I know both the provers and maintainers, so I'll press them.
**jmacdonald** 27:34 Thanks, Mike.
**Chris Marchbanks** 27:35 It's not approver approval, it just.
**jmacdonald** 27:37 I mean, actually, like, if you want to go review it… Honestly, that would… that would be nice, too.
**Mike Goldsmith** 27:42 Sure.
**jmacdonald** 27:42 Since I know you do go. Thank you.
**Chris Marchbanks** 27:46 Thank you.
**jmacdonald** 27:46 Cool.
That was progress. Thanks, Chris.
I'm gonna put your name on the list here. Okay, anybody, last call?
Nope. Alright, thank you all. Two weeks from now, chances of me being here are pretty small. I'm not on a vacation, so… Or it's my birthday, or something like that, one or the other.
So don't count on me two weeks from now, but a month from now, Definitely see you.
I'll try to remind people that I can't make it in case you don't want to come. Like, I don't know. I don't… you don't need me to have a meeting, though, so thank you all.
See you next time, 2 or 4 weeks from now. Cheers. Happy summer.
**Otmar Ertl (Dynatrace)** 28:25 Thank you, bye.
**Yingrong Zhao** 28:27 Thank you.
