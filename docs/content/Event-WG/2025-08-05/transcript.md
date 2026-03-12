SIG: Event WG
Date: 2025-08-05
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/CHsQ5dQIVnn4_-STvyH0YC8MuoY68iGmek2pFWxrznVxIAxZnRDvgEx1-6c-Ywrn.SkiMf7SdFrytR5m7
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:43 Hey! Antoine.
**Antoine Toulme** 00:45 May we meet again.
**Trask Stalnaker** 00:47 Yeah.
**Antoine Toulme** 00:50 I'm just curious at these points. I wanna attend some of the CC. What's up.
**Robert Pająk** 00:56 Oh!
**Antoine Toulme** 00:58 I work which.
**Robert Pająk** 01:14 1st you want to pull your declarative config topics.
**Trask Stalnaker** 01:19 Yeah.
**Robert Pająk** 01:20 You can put above mine if you want.
**Trask Stalnaker** 01:27 I think we have plenty of time.
**Antoine Toulme** 01:34 Go ahead!
**Trask Stalnaker** 02:02 All right.
Event. Name attribute reserved.
Right?
Cool. Yeah. Definitely makes sense. I think we should have some Dean, can you kind of talk about the scoping difference between scoping it under the hotel namespace and other things that are scoped there today.
**Robert Pająk** 03:04 If you go to, there's a hyperlink in the proposed. In the 1st I put a hyperlink also attributes registry. Yeah, it's here. So initially, I wanted to keep just event.name. But then I saw, yeah, all of these things which looks more appropriate. It also avoids potential collision. If someone already uses event name, which kind of is very generic.
might be generic and also wouldn't collide with the deprecated event name which was there before. So because I have forgotten to call it out that. Yeah, that also. Yeah, because event name is right now deprecated.
And also, I think that this underscore, you know, is currently the convention on separating words, not the dot which was before events.name. But I think the reason before was that it was a scope for events.
any trust means here.
Are you here, or are you.
**Trask Stalnaker** 04:07 Yeah, I I'm here. But my video seems slot.
**Robert Pająk** 04:12 This is important.
**Trask Stalnaker** 04:14 Oh, okay, So event. I think that the convention is.
I think, would be event.name, hotel.event.name We've got hotel dot span in general. We do the dots instead of underscores. We only do underscores. If it's between 2 words that like make up a We don't.
The 1st one isn't. That's hard to describe. There's some wording about it.
this one. Maybe we would have done dots in retrospect.
**Robert Pająk** 05:09 No, I think it's fine status quo to be honest.
And then, yeah.
okay, so I will edit the description, and also added an alternative namings, which will be one of this underscore, and also without the auto prefix. I will do. After the meeting.
**Trask Stalnaker** 05:32 Okay.
**Robert Pająk** 05:34 And I will also update the Pr which already has 2 approvals in.
**Trask Stalnaker** 05:41 Oh, gotcha.
yeah, yeah, no. I think it's the use case is strong. And like, you said, it's for People who want to use their existing loggers to emit events is the.
**Robert Pająk** 06:08 Previously. It was on my mind, but I never created it. But recently a user explicitly asked for it.
That's why I decided it's time for for it.
**Trask Stalnaker** 06:22 Looks good to me.
allow adding new attribute types. Yes, this is the complex attribute.
**Robert Pająk** 06:37 So we discuss it also during the specification meeting here. I mostly wanted to ask if there's anyone here who has some. You know time. Personally, right now I'm very swamped.
And yeah.
and this fastest I could probably touch. It will be probably something like in 2 weeks. My guess.
Ludomywa said that she might be able to start working on it.
But I think we can probably maybe create subtasks for it like, and I was just thinking that maybe here we can come up with this ideas we know about this blog post, which could be one thing, maybe with some draft Pr which will be referenced in the blog post. I'm not sure if we want to do anything in this, the specification changes, you know, changing this text, which right now requires the major bump. I think these are the 3 subtax which comes to my mind right now. But maybe we could somehow maybe separate. Do you have any any. What do you think to ask Antoine any? Do you have some opinions here?
**Antoine Toulme** 07:49 No! The heat.
**Trask Stalnaker** 07:51 Is this covered by your own? Your proto pr. Already.
**Robert Pająk** 07:58 No, it's not. I didn't want to scope it.
**Trask Stalnaker** 08:01 Add a note that introducing new attribute types will require a minor version bump.
so as opposed to a patch.
**Robert Pająk** 08:12 Just saying that it can't be done in a not a major. Before. In the specification it was called out that it will be a major, a major, but I'm not sure if we need to.
**Trask Stalnaker** 08:24 What about?
**Robert Pająk** 08:25 I think this note.
**Trask Stalnaker** 08:26 He.
So I.
**Robert Pająk** 08:30 Go on, trust.
**Trask Stalnaker** 08:31 Yeah. I agree that the we should do a Pr to the spec repo to update that language.
**Robert Pająk** 08:40 Yes.
**Antoine Toulme** 08:42 Sure.
**Trask Stalnaker** 08:44 Instead of require, I would say, may be done in a minor version. Bump.
But I wasn't.
I'm not following the Otlp. Change the change to the Otlp proto repo that you want to make.
**Robert Pająk** 08:59 I don't. So my only idea right now was to make a draft Pr on the proto that will be referenced in the blog post. And this Pr would just remove all this type restrictions.
basically to remove the lines which I'm adding right now in my current. Pr, that is my current idea.
**Trask Stalnaker** 09:21 Yeah, and don't we.
**Robert Pająk** 09:24 And it will be like open for this. I don't know 3 months period, or something like that.
but I think it may be a good way to communicate it. What the blog post means to think it, and also we do not need to rush with merging it. We can just, you know, merge it in 3 months, when everybody is online.
got it.
**Trask Stalnaker** 09:49 Yeah, So let's look at your current.
Pr.
**Robert Pająk** 10:01 So after this is merged, I just wanted to remove all of this.
Basically, you know, reverse it. And then, right now, before it's not merged. I cannot make even a Pr. For it.
**Trask Stalnaker** 10:14 Right.
So already in here you mentioned, these can change.
**Robert Pająk** 10:19 God.
**Trask Stalnaker** 10:20 Final release.
**Robert Pająk** 10:21 Yep, so it's already addressed. I have forgotten about it. I, after 2 weeks.
**Trask Stalnaker** 10:28 But right then, at some point we would remove these at some point.
**Robert Pająk** 10:43 And right.
Yes, exactly.
**Trask Stalnaker** 10:47 Or essentially, you would remove all of the all of.
**Robert Pająk** 10:50 No, not really, because they're also this key value, that the that repeated keys may be problematic.
And that's why I would key just remove the ones that use selected from 3, 8, 1 to 3, 8, 5.
Yes, I will just remove this.
**Trask Stalnaker** 11:12 Oh, I see keeping the I see. This still applies to this text.
**Robert Pająk** 11:17 Yes.
**Trask Stalnaker** 11:17 Here also.
**Robert Pająk** 11:18 Yes.
**Trask Stalnaker** 11:19 Got it.
Okay.
Makes sense to me.
I think so we would. Our goal would be to merge this before the blog post.
**Robert Pająk** 11:46 Give me!
**Trask Stalnaker** 11:47 Put up a draft at least of removing these, and we would point to that Pr that open Pr in the blog post.
**Robert Pająk** 12:00 We could also maybe create a draft Pr for the specification changes. I can also try doing it like a something like a Poc, which also changes. You know the Api Sdks, something which will look like the end goal. How the specification would look like in 3 months.
**Trask Stalnaker** 12:21 Yeah, let's I think it would be good to have the corresponding to this in the spec repo exactly cause that will be very targeted.
Not finding it.
**Robert Pająk** 12:40 I already created a Pr for adding empty. But I could probably work on creating a specification Pr, which would add all of these complex attributes, and just mark it as a draft. I just didn't want to put everything you know as a Pr, because it will be a huge scope if pull request. Yeah. Blocked.
Drift from the top in the pull requests.
**Trask Stalnaker** 13:05 Yeah, what I was looking for is does that? Does that cover the change to the standard attributes.
**Robert Pająk** 13:14 Yes, it does, and also in a few other places. It's not. I think it was not the only place where I had to make the change. So it's easiest to go to the pull request and see the changes blocked at empty value attributes. 5.th From the top you can see my face.
I try to assign myself to easily find myself.
**Trask Stalnaker** 13:46 Okay, but it. This is not changing the text about it being a major bird.
**Robert Pająk** 13:53 No, no, wanted to remove it and create a separate Pr. For it.
**Trask Stalnaker** 13:58 Yeah, that's what I was thinking. The p to me, the corresponding Pr to this pr in proto is the Pr in spec that just removes that language.
**Robert Pająk** 14:15 Yep.
**Trask Stalnaker** 14:17 And then, if we merge both of those, I think it would be good to merge both of those first, st and then have.
**Robert Pająk** 14:26 Yes, draft pr up.
**Trask Stalnaker** 14:30 For, and point the blog post to those draft Prs.
**Robert Pająk** 14:34 Yep, I agree.
**Trask Stalnaker** 14:38 Cool. I'm out tomorrow through the rest of the week. But let's touch base next week. In this meeting I should be able to help with some of that.
**Robert Pająk** 14:54 Oh, 3, 2, add some notes.
A at it was cool.
We can just bump it to the I'll okay.
**Trask Stalnaker** 15:04 Next week's agenda already.
Cool.
Sounds good.
Anything else you wanted to chat about on the on this.
**Robert Pająk** 16:38 No, it's good enough. Thanks.
**Trask Stalnaker** 16:47 So for.
So I think, based on feedback in today's meeting, at least that I'll proceed with this version.
It doesn't mean that like I, said I, I honestly think they could both. They could coexist like if there's if the collector.
**Robert Pająk** 17:18 Also in my original author. But there were also some people who didn't like to at the same point of time. But I yeah.
that eventually people still may need it. The question, like, my main question is regarding this pipelines and collector. If it's something critical or not, I don't know if this is something that Antoine may know or follow up with.
**Antoine Toulme** 17:42 No doctor has no idea but we could look into it.
The collector.
We have an entities discussion, right? There is also for that.
Am I right?
**Trask Stalnaker** 17:56 What? How do you? What do you do? Do you have a like a log filtering concept in the pro in log filter processor, in the collector.
**Antoine Toulme** 18:06 Like a way to
**Trask Stalnaker** 18:09 Logs.
**Antoine Toulme** 18:10 To drop logs. So we have multiple things. There are multiple processors, and mostly in country, we have one which I contributed to, which is a probabilistic sampler which allows you to pick a resource attribute of your choosing as a source of.
let's say, the source of sampling, and or you can also sample on other things on your on your log and then you can apply a percentage of what you want to sample to right and choosing.
It's using head sampling, using some math to just do the hash of whether to keep it or not.
It's great because it works in a horizontal scaling scenario. Then you have tell sampling which I don't know that is doing that much for logs. There's a deep dap.
I think the ddop might be using some version of a bloom filter to just make sure that we don't have twice the same log. Come in.
I'm actually less sure where it's at. At this point.
Log data processor is still in Alpha. It's not deployed anywhere.
**Trask Stalnaker** 19:14 What if some.
**Robert Pająk** 19:14 Do you know where the clarity is? The one which is in this pack is used in collector? The only place which I am aware of is the Service Telemetry.
I think this is the place right.
**Antoine Toulme** 19:31 But for the longest time the character didn't have a really deep log story, as of 2 months ago. I think we started to see some activity from some receivers actually producing logs in some format that was actually understood, that looked more like events. And maybe the only one that's meaningful here would be the SQL. Server receiver, which is now emitting slow queries. Logs.
Does that make sense?
And actually events right? They're they're meaningful events. So we could apply some some level of the spec of how we want to produce them, so that they're mapping to the format you expect, and they have the attributes that you want to see in that spec.
**Trask Stalnaker** 20:14 Is there? How would if a user came to you and said, I want to in my collector, I want to drop any. All the info logs.
**Antoine Toulme** 20:25 So you would use the transform processor which is using open telemetry. What's Tl is?
Let's see.
**Trask Stalnaker** 20:33 Yeah. And she's language, I know.
**Antoine Toulme** 20:36 Oh, yeah.
and then you can do all sorts of random stuff like that where you say, drop delete when this attribute has this value right? And they're trying to make it more programmatic than just severity or whatever. So this is.
**Trask Stalnaker** 20:50 Yeah, yeah, that's a legitimate way to do it. Yeah, yeah.
**Antoine Toulme** 20:54 There's another old one called the Lux Transform Processor, which never is going to come out of development because it's supposed to be supplanted by the transform processor.
Yeah, the other thing that happens a lot is, why would you even get those logs right? So the file log receiver, which is the main way we would ingest logs is by reading files is also allowing you to have what he calls operators that can affect the source of the data. So you can parse the data. You can drop data. You can do all sorts of things. And this way, you're not even reading from the file things that you don't care to even process.
**Trask Stalnaker** 21:35 Yeah, I guess it would be, for if it's receiving from.
**Antoine Toulme** 21:40 Yeah. Gateway.
**Trask Stalnaker** 21:41 50 K's.
**Antoine Toulme** 21:42 Yeah.
**Trask Stalnaker** 21:43 But again in the sdks it's more efficient to push that decision upstream to the SDK itself.
**Antoine Toulme** 21:51 It. It might. Yes, I mean, it depends a little bit on some of our. You can see it in complex customer bases where there is a separation of duties between.
Maybe the development team does not care, and we like to get everything. The gateway is going to do all sorts of schemes to reduce the.
**Trask Stalnaker** 22:10 Noise. Yeah.
**Antoine Toulme** 22:12 I don't know if you guys saw there is a very intriguing proposition that was made 3 days ago on slack by someone who came and said, I have a isolation forest processor that is going to be able to work for any signal can take data from traces. Metrics like say, look at a corpus of metrics and apply a this algorithm to find out if a log or metric is an analysis where they are outside of the general population of what we would see usually.
**Trask Stalnaker** 22:45 That's great!
**Antoine Toulme** 22:46 I'm I'm excited about it, like, from a the nerdy point of view.
I don't know if it works. I don't know if it's good.
Yeah, right? Right? It's yeah. But I'm using.
**Trask Stalnaker** 22:55 Magic. If if you can make that work great, then you've made magic.
**Antoine Toulme** 23:00 Right? So this has. This is what we do in the collector is more like.
can we do this really wonky approach of like collecting a slice of data for 30 seconds and pick something from it that is going to give us insights about what's going on.
Yeah. So we're almost like a different domain where yeah, filtering is.
I'm not gonna say it's not exciting, but it's it's something that is done, usually in a transformation that yeah, it's not too much work.
So so one of the probably one of the best, like most applied use cases of the transform processor.
**Trask Stalnaker** 23:45 Cool I mean. So I think we have a pretty clear path forward.
**Robert Pająk** 23:53 I also want to point. Have you been at the configuration seat discussing it or not? Really this proposals?
Because what I saw in your Pr. For this more, declared Locker. Configuration that it has some hearts.
and it also I don't remember. I remember that also heard from Tyler and Jack. Yeah.
yes, which looks like they are fully favoring it. I know that Tyler had a different opinion previously, so given given his opinion, like, I also do not have any strong opinion here. It may be our desire to go this way, and also it will motivate to go, seek to implement the logo configuration. Maybe.
**Trask Stalnaker** 24:43 Cool. Yeah, this is my preference also, as far as the place to start.
So I will. Yeah, I will just check over this once more and make it ready for review. And I'll probably just close this one with a comment that we can revisit it in the future after cause. Yeah, I think if we try to do 2 at once, people will get kind of panicky about that.
**Robert Pająk** 25:19 I agree.
**Trask Stalnaker** 25:24 So I will update my. I will send a new Java proof of concept for this for the alternative.
Alright, let's leave now. We're done.
**Jason Plumb** 25:53 That we're not triple booked.
**Trask Stalnaker** 25:57 Hey Jason.
**Jason Plumb** 25:58 Hey? Sorry.
**Trask Stalnaker** 26:01 Wait now. It's like a splunk party.
**Jason Plumb** 26:04 Yeah. Splunk party woo.
**Antoine Toulme** 26:09 You, wanna you wanna switch over to Webex for asking.
**Jason Plumb** 26:14 Oh, it hurts, it hurts cause it's true.
I'm like weirdly punchy this morning. I think the coffee's kicking in.
**Antoine Toulme** 26:26 Yeah, it's a good time of the morning to just this is like the half hour when you finally, everything's working the coffee like, worked.
Ugh! Okay.
Jason, you have anything.
**Jason Plumb** 26:43 Yes.
**Antoine Toulme** 26:44 Oh, right!
Let's do it. Let's go.
**Trask Stalnaker** 26:47 Yeah.
**Jason Plumb** 26:48 I have to shake out these cobwebs. There was something we talked about last Thursday, Trask and I forget what it was.
**Trask Stalnaker** 26:57 The.
**Jason Plumb** 26:58 We are.
**Trask Stalnaker** 26:59 Yeah, was it the proof of concept for the server? The log record processors.
**Jason Plumb** 27:04 Yes, and I haven't looked at it yet.
**Trask Stalnaker** 27:07 That's okay. Cause we're going in a different direction.
**Jason Plumb** 27:11 Phew! I dodged that one.
**Trask Stalnaker** 27:13 So there will be a new. I will send a new a new Java poc for the alternative. We discussed it in the spec meeting today.
**Jason Plumb** 27:25 Oh, okay.
**Trask Stalnaker** 27:27 We're gonna I sent 2 different spec, Prs, so yeah. So that won't happen. I'm out tomorrow for the rest of the week. So.
**Jason Plumb** 27:41 Cool.
**Trask Stalnaker** 27:42 That'll happen sometime next week.
**Jason Plumb** 27:44 You're out for the sig as well.
**Trask Stalnaker** 27:46 Yeah, I need to announce that.
**Jason Plumb** 27:49 Maybe Watson can run it or something.
I don't think Laurie is back.
I mean, I could run it. Yeah.
**Trask Stalnaker** 27:58 Cool.
**Jason Plumb** 28:01 Cool.
**Trask Stalnaker** 28:04 All right.
Alright. Well, thanks for joining for and saying, Hi, Jason.
yeah. Sorry. Sorry I was late. I that as it's written on the page right now. It says, AI Trask.
Yes, action item.
**Jason Plumb** 28:20 No, no, that's not what that.
**Trask Stalnaker** 28:21 Oh, that's true, I know.
**Jason Plumb** 28:26 Agentic. Trask.
Cool. Well, have fun on your vacation, whatever you're doing.
**Trask Stalnaker** 28:34 Thank you. Going to Montana. Visit my sister.
**Jason Plumb** 28:37 Oh, fun, sky, country.
**Trask Stalnaker** 28:40 Yes. Yes.
See ya.
**Antoine Toulme** 28:46 Everyone take care!
**Jason Plumb** 28:47 Bye.
**Robert Pająk** 28:47 See you.
**Jason Plumb** 28:48 See you.
