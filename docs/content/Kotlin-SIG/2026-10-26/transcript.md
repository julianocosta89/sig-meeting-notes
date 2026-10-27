SIG: Kotlin SIG
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jamie Lynch (Palo Alto Networks)** 02:45 Hey, everyone.
**Jason Plumb** 02:49 Let's see what my background is, I wonder.
Okay, I saw the twins, good, okay.
**Jamie Lynch (Palo Alto Networks)** 02:55 Silver.
We'll paste the doc link in the chat, so if anyone does have items, please add them to the agenda here, and we'll get started in a couple of minutes.
**Juan Vega** 03:31 Hello.
**Jamie Lynch (Palo Alto Networks)** 03:34 Nope.
**Jason Plumb** 03:35 Hello.
**Hanson Ho** 03:58 Let's see, this meeting is still in Pacific time.
**Jamie Lynch (Palo Alto Networks)** 04:04 Yes.
**Hanson Ho** 04:08 I guess this means it'll be… An hour… later for me? Next week?
Yeah, fall, fall back.
Yeah.
**Jamie Lynch (Palo Alto Networks)** 04:22 Is it this year that they're just not moving the time in Vancouver?
**Hanson Ho** 04:26 Supposedly indefinitely. So, we are perpetually daylight saving.
Or saving daylight. So, yeah, I don't mind.
**Jason Plumb** 04:37 How does that work with time zones? Are you still considered… Pacific Snow? Is it its own thing now?
**Hanson Ho** 04:43 It's funny enough, called, I think, PCT.
commercial time.
**Jason Plumb** 04:48 Oh, Pacific Canadian time.
**Hanson Ho** 04:50 It's not Canadian.
**Jason Plumb** 04:52 It should be Cascadia time.
That would be good, because then we could join it, I want in on this.
**Hanson Ho** 05:00 yeah, it's it's gonna be annoying initially, I think, but I think I'm gonna like it.
I can sleep for another hour, instead of getting up to watch football at 7am on Saturday, I get to get up at 8am. Sometimes, 5.30am, so… yay.
**Juan Vega** 05:22 Where are you, Hanson?
**Hanson Ho** 05:25 I mean, thank… well, Jason, yes.
**Jason Plumb** 05:28 You were asking me, yeah, I'm in Portland on the West Coast, so I'm just like…
**Juan Vega** 05:31 Oh, sorry, I meant, I probably said your name wrongly.
**Jason Plumb** 05:34 That's fine, Hanson, yeah, they sound alike with an accent, it's fine.
**Hanson Ho** 05:38 I'm in Vancouver, Canada, so, if you have,
**Juan Vega** 05:41 You were before.
**Hanson Ho** 05:42 in British.
**Juan Vega** 05:42 Columbia And you have changed for… so you have already discussed the idea of going back to… Day flight saves time for the whole country, or it's just your…
**Hanson Ho** 05:56 It's just my province, and.
**Juan Vega** 05:57 How are you, friends.
**Hanson Ho** 05:58 Manitoba is as well, but not a lot of people work with folks from Winnipeg, or Brandon. So it's, it's, it's… really Vancouver, that's, that's, impacting, at least our industry.
**Juan Vega** 06:15 No, I have a fellow in… a teammate in Vancouver Island. It's not the same as Vancouver, but it's… it's close, no?
**Hanson Ho** 06:23 Yes, exactly, exactly. They're gonna be, an hour offset. Unless you're in Argentina, in which case, you know, you… then you never change. There's certain places.
**Juan Vega** 06:31 No, no, I am in Europe, actually. So, for me, it's like, 8 hours, I think, right now? Or 9? I don't know, I never know.
**Hanson Ho** 06:43 Yeah.
**Juan Vega** 06:44 Portland is 9 hours, and Bakura is maybe 1 hour.
More, no? Or 1 hour less.
**Hanson Ho** 06:50 It will be next week, Vancouver and Portland.
**Juan Vega** 06:53 Yes.
**Hanson Ho** 06:53 Seattle and California used to be the same time zone, and we changed at the same time, but this year, we introduced this new thing where we don't change. Hopefully, Portland goes along with us.
**Jason Plumb** 07:04 I think all of these… I think all of the major, like, cities at least, I think all of the states along the West Coast, like Washington, Oregon, California, were pretty well set up to align.
But I don't know where that stands right now.
**Jamie Lynch (Palo Alto Networks)** 07:24 Cool, or you can just make a start on the issues, it's relatively light, so if folks do have stuff they want to discuss, please feel free to… Add items to your agenda.
So, first up, I thought I'd just give an update with the propagation API.
So… I think I've… updated it so that it's possible to create propagators and non-recording spans, etc, from the API.
without needing an OpenTelemetry instance. The remaining thing is just… Figuring out how we manage, creating a context, and… How bits are stored, in that context.
So, I think I'll try and have a look at that for what started this week, Yeah, I don't think that really requires action, just, like, an update.
**Hanson Ho** 08:33 And we'll get all the PRs this week, or not this week, today.
**Jason Plumb** 08:38 I think that propagator's thing will make Carlos very happy.
**Jamie Lynch (Palo Alto Networks)** 08:42 Hope so. Or maybe it'll be a Christmas present.
**Jason Plumb** 08:46 Oh, boy.
**Jamie Lynch (Palo Alto Networks)** 08:46 If it gets done by then.
**Hanson Ho** 08:49 Hopefully it's a Halloween present, but, you know…
**Jamie Lynch (Palo Alto Networks)** 08:54 Yeah, I mean, the other thing I wanted to go back to is I've added a few more issues to this ContribFest.
label now. Yes, we've got about 7 in total. I think 2 are just docs.
Changes, but the others… Tried to keep them reasonably… Isolated and possible to do with, like, Maybe less than an hour.
**Jason Plumb** 09:20 Cool.
That's awesome, thanks for doing that.
Yeah, I'll definitely take a look at these, I think… I mean, KubeCon is coming up in, like, 2 weeks, so it's pretty quick.
**Jamie Lynch (Palo Alto Networks)** 09:32 Yeah. Yeah, it'll be interesting to see.
To see if folks pick that up, because, yeah, that'd be great, getting more people interested.
**Hanson Ho** 09:44 It's amazing we're at number 1,285 already.
**Jason Plumb** 09:49 For PRs, yeah, or for…
**Hanson Ho** 09:51 Yeah.
**Jason Plumb** 09:52 Yeah.
They go by quickly.
**Jamie Lynch (Palo Alto Networks)** 09:58 Cool. Well… That was all I had. Did anyone else have anything they wanted to discuss?
**Jason Plumb** 10:08 Now, should reviewing the propagators, is that the best place for us to spend time right now?
**Jamie Lynch (Palo Alto Networks)** 10:16 Yeah, I think I would… Definitely help in terms of… Yeah, moving, like, the… moving the project towards stabilization.
There's also… Like, a few PRs.
coming in from, like, other contributors, but I think Publicators is probably what we should be focusing on.
**Jason Plumb** 10:36 Okay.
Cool.
**Hanson Ho** 10:39 maybe after KubeCon, we should just take a look at the roadmap and see where the next big chunk of stuff that we want to take on is, once we have whatever we have outstanding to be stabilized, so…
**Jamie Lynch (Palo Alto Networks)** 10:54 Yep, sounds good.
**Jason Plumb** 10:56 Sounds good.
**Jamie Lynch (Palo Alto Networks)** 11:00 Cool. Nice and short meeting this weekend.
**Jason Plumb** 11:05 into it.
**Hanson Ho** 11:07 He's a good…
**Jason Plumb** 11:08 Yeah, plenty to do on a Monday.
**Jamie Lynch (Palo Alto Networks)** 11:10 Yep. Alright.
**Juan Vega** 11:11 Yeah. Bye.
**Hanson Ho** 11:12 Thanks.
**Jason Plumb** 11:12 Thanks, everyone.
**Juan Vega** 11:13 Bye-bye.
