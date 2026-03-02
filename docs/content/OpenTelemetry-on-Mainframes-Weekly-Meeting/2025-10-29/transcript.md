SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-10-29
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 01:37 Hey, Greg, how you doing?
**Greg Shriver** 01:42 Hey, Jim, I'm well, how are you?
**Jim Porell** 01:45 Alright.
Sounds like we should have an interesting conversation today.
**Greg Shriver** 01:52 Yeah.
And I assume this is… This is for the Open Telemetry Collector.
on Linux, right?
**Jim Porell** 02:10 Yeah.
Nope.
**Greg Shriver** 02:11 Okay.
**Jim Porell** 02:12 I also think some of this is needed
for our PRs to actually be approved and shipped, so I think…
I think we gotta talk about both parts of this.
**Greg Shriver** 02:24 I see. Okay.
**Jim Porell** 02:26 Yeah, because I think we're, you know, we're doing this… the whole semantic convention naming in phases.
But we're kind of at a place where a lot of this stuff can be approved. I think you approved some of the PRs.
But have they been adopted, you know, by… headquarters SIG, if you'd like.
**Greg Shriver** 02:45 Yeah, I had…
**Jim Porell** 02:47 Headquarters means.
**Greg Shriver** 02:48 Yeah, all the stake… all the stakeholders, right? Yeah.
**Jim Porell** 02:52 Yeah.
**Greg Shriver** 02:55 Yeah.
**Jim Porell** 02:56 It's really funny, I was just talking to the product owner for Omegamont, and he's like.
I want us to agree on TMON naming and Omegamon naming going into the future. I go, what do you think OpenTelemetry is? And BMC is going to agree, and so is Broadcom, and we'll have common naming for all metrics, so that other products can easily absorb
mainframe data, regardless of source. He goes.
I didn't know that. I'm like…
Why do you think I'm in these meetings?
**Greg Shriver** 03:29 Right, yeah, that's why you're spending this time, yeah.
Oh, but, you know, I mean, it's a fair point. I mean, I suspect…
I mean, I… you know, I certainly don't want to say that on a public forum, but, you know, I mean, we… Broadcom has its own, you know, disharmony, right?
**Jim Porell** 03:48 Oh, yeah, absolutely.
**Greg Shriver** 03:49 I mean, and I think, you know, we're gonna have to attack that.
internally.
and in the SIG, and then to all… to the community stakeholders. It's really a three-tier process, and it's gonna be slow, and it's gonna be a lot of work, and it's gonna take time.
And this is not the thing that's going to be done next week. It's just…
**Jim Porell** 04:12 I know we're being recorded, but…
between you and me, what IBM's doing with the subsystems.
how is that even going to work without the naming conventions adopted yet? So they can pump out open telemetry stuff. I guess they can get a span ID out, but…
**Greg Shriver** 04:28 Right.
**Jim Porell** 04:30 who's doing anything with that data? And…
**Greg Shriver** 04:33 Well… I mean, you could fix it, though, because there's… there's the piece that takes…
the span data that's generated before it gets emitted to the OpenTelemetry collector.
And the other option is, you know, and we do this as well, the other option would be to have, like, an edge collector that uses OTTL and transforms the metrics
You know, before it goes… before it goes to an external… before it goes to, like, a gateway collector. I mean, so…
**Jim Porell** 05:06 to me, the span ID, what you just said, the span ID is the secret sauce, because that allows correlation. For sure. If you can… if you can do correlation, then proprietary metrics work fine, but it's really all about getting the correlation done.
**Greg Shriver** 05:21 Yeah. And being able to show that application perspective.
I mean, yeah, no, I agree with you, I agree with you, Jim. I just think,
You know, dealing with the inconsistencies of
you know, of what we're naming things versus what the OpenTelemetry standards
say that they should be named. That's going to be an ongoing problem, and even… even.
**Jim Porell** 05:48 Oh, yeah.
**Greg Shriver** 05:48 Even if we had it, like, buttoned up and tied with a bow today.
Tomorrow, it's gonna change, right? Right.
**Jim Porell** 05:56 We still have to wait n amount of time for each vendor, and I'm talking Dynatrade, Datadog, Splunk, whatever, to adopt the standard. Right. They have to adopt it and be able to have dashboards accessible that will accept our naming, you know?
**Greg Shriver** 06:13 Exactly. And then you've got customers that are using those observability backends that have dashboards that they've created, right?
**Jim Porell** 06:22 Right.
**Greg Shriver** 06:22 And so, you know, the observability back-end vendors are kind of, you know, they can't just willy-nilly make a change, because it's going to impact their customers, so…
**Jim Porell** 06:32 It's gonna be a slow-moving kind of, you know, caterpillar. It's gonna be a slow-moving train.
And by the way, that's true to an extent,
we've done open telemetry via Omegamon, and we put in
here's the ZOS metric, and there's an AS clause that says, you can name it whatever the hell you want.
**Greg Shriver** 06:57 And…
**Jim Porell** 06:58 The cool thing is.
because it's all JSON ready, the tools on the back end, in SCA and Splunk, can recognize those names, and we'll build the dashboard with that name. So whatever name you want it to be, it can be. Now, at some point.
We'll stand… we'll use the standard conventions to… or the common semantics to say, alright, you don't need… you don't need to do it yet.
Unless it's stuff that hasn't been identified yet, then you can do your own magic on there, but .
**Greg Shriver** 07:30 Sure.
**Jim Porell** 07:32 Yeah, it's kind of… it's kind of crazy.
**Greg Shriver** 07:35 Yeah.
That's funny, I just… I just got a…
a message from Antoine Tomey, I don't know if I'm pronouncing his name, he says…
**Jim Porell** 07:49 Oh, no, yeah.
**Greg Shriver** 07:50 Yeah, Morgan says he's triple booked, so he can't make it, and Antoine said he's only double booked. That's awesome.
**Jim Porell** 07:58 And then Rudiger, who advertised on Slack that he's coming, isn't here. Isn't here yet. For the whole purpose of solving these problems, so… I mean, I can actually text him, yeah, I can text him, let me see.
**atoulme** 08:12 Nice. Yeah, I mean, I think this is really a vexing issue, just related to administrative privileges. Let's just fix this stuff, and…
I… I am not the person who can fix this. The only person who can really have administrative access to the GitHub project is going to be Trask.
And maybe a couple other people who are in that situation. And that is…
we just need him and Riddigger in the same space for 5 minutes to resolve this.
**Jim Porell** 08:38 Yeah, right.
**atoulme** 08:40 They have a…
they have an outstanding meeting on Thursdays, like I mentioned, where we just talk about infrastructure itself.
And, if I don't hear back from Rieger, I'm happy to bring it up to Trask tomorrow, if I can join at 11.
just to push a little bit harder, but Trask is asking clarifying questions like, hey, who's going to be responsible for this? Can I put them up as responsible? And it seems like Ridiger's saying that he needs to be administrator on the organization so he can have
the level of privilege required to make this happen. So we're now stuck in where both of them have half the solution.
Someone's gonna have to give… I don't know how that work.
I don't think the Microsoft employee who is Trask wants to go and get an IBM ID attached to his Microsoft email.
**Greg Shriver** 09:26 Right.
**atoulme** 09:26 So now we're… I don't know what we do.
**Jim Porell** 09:29 Yeah, okay.
**atoulme** 09:32 You know, I'm in the middle of this, and I don't know what to do to help more than just, you know.
**Jim Porell** 09:37 Whoa.
**atoulme** 09:37 Messages back and forth between those two guys, because that's the…
And Travis is very competent and nice, and he'll do whatever we ask him to do, but…
It's… it's asking the personal commitment of him, which is…
**Jim Porell** 09:50 zoom.
**atoulme** 09:51 Let's step two.
**Greg Shriver** 09:52 Yeah, I get that.
**Jim Porell** 09:54 So, Rudiger's showing he's online at work on IBM's side,
And available, but he's not responding to messages, so…
**atoulme** 10:04 It's funny. So…
**Jim Porell** 10:09 And I told him it's the three of us on the call waiting for him.
No pressure. Yeah, yeah, right, exactly.
Oh, boy.
Yeah, I don't know what else to say on that.
**atoulme** 10:30 Perfect, we can drop. We can… well, I'll invite Rudiger to the Infra meeting tomorrow as punishment, because it's one hour later.
That's heavy.
**Greg Shriver** 10:40 Skip for him.
**Jim Porell** 10:42 It's 6… it's 6 p.m. for him this week, because they already changed… well, in Europe, they changed times.
**Greg Shriver** 10:48 Oh, they've changed.
**Jim Porell** 10:50 Well, it's a 5-hour difference instead of a 7-hour difference, or a 6-hour difference. That might be the problem.
**Greg Shriver** 10:56 He might be thinking it's… Oh, he might be…
**Jim Porell** 10:59 An hour later, but who knows?
**Greg Shriver** 11:00 Yeah.
**Jim Porell** 11:02 I always like that with going to church, all these people that either show up an hour late or an hour early on the Sunday, the time changes.
**Greg Shriver** 11:10 They do that on purpose. Oh, I missed it, sorry.
**Jim Porell** 11:12 Yeah, exactly.
**atoulme** 11:17 Get me out of bedroom early. I don't know what I'm gonna do.
**Jim Porell** 11:20 Yeah, right.
**atoulme** 11:21 A little bit tough.
So, I'm gonna just add him to the other Slack channel that is related to Project Infra.
Okay. And I'm inviting him to the meeting tomorrow, and that's all I can do.
**Jim Porell** 11:35 Alright, thanks, Antoine.
**atoulme** 11:38 No problem.
**Jim Porell** 11:40 Right, I guess.
**atoulme** 11:41 I'll drop now, I have to go back to my other…
**Greg Shriver** 11:44 Another meeting, yeah.
**Jim Porell** 11:45 I think we're done, yeah, alright.
We'll see you guys next week.
**Greg Shriver** 11:48 Alright. See you later. Thanks, guys.
