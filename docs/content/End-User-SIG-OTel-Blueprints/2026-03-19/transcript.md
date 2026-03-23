SIG: End-User SIG: OTel Blueprints
Date: 2026-03-19
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/GUy8oAQHgh9UBFQjgoJo-i0ctCsX86fGFLCq2G7vD3TpbO9j45pXk6-mZHcqmL4.p3YwJtD1XXEWf3xr
============================================================

## Zoom Recording Transcript

**Tiffany Hrabusa** 02:18 Hello.
We may have had some time zone confusion, so we'll give it another couple minutes, and see if anybody else comes.
**Dan Gomez Blanco** 03:11 Hello, hello?
**Tiffany Hrabusa** 03:12 Hello.
**Dan Gomez Blanco** 03:22 I have reached out to Hope with a friendly message, but I think… It was not received. Or not our knowledge, actually, but… That's what I mean.
**Tiffany Hrabusa** 03:30 It just…
**Dan Gomez Blanco** 03:31 Login.
Alright.
I'll give, a couple minutes for people to join in, to put any topics on the agenda. I'll share the notes in the chat.
Okay, we can probably start. I saw the message from Lukash, but Not sure if he's gonna be able to join… I wonder if that's related to… people… sink in there.
Invites.
In different ways, as in, like, if it falls out of, Not sync.
**Tiffany Hrabusa** 07:54 I think there's always a bit of confusion when we hit this time change period.
**Dan Gomez Blanco** 07:59 Yeah.
Yeah, I guess that could be it as well, yeah.
M… I can share my screen.
And we can go through.
Through the notes, Cool. So, yeah, let's go first through the… Board and do a quick view.
So we have, yeah, we have merged that, so we've got a blueprint template, things in progress.
I think I can probably assign this.
If I open the actual issue… Wonder if I can assign it.
Yeah.
Gotta sign in.
So I think Lucas is being… is putting together a… A draft.
Right, just… I want to make sure that I'm not missing anything that's… I don't want to go into every single item, but, like, just to make sure that we've got everything that… that we are yeah, everything that we're doing here. So we've got the… Yeah, this blueprint that is currently in progress, there is a draft from Lucas that it's asking people to review.
Mmm… I guess the idea, yeah, is just to give it a first pass.
And then, I have added some comments on it.
Yeah, give it a first pass before we… Before we open the PR.
If people can review that, that would be great.
This one, I have not started on this, but I plan to start.
just after… well, maybe during KubeCon, or next week, or the week after.
I plan to start on this one.
Yeah, things have been a bit hectic in the run-up to KubeCon, as usual.
M… blueprint for Kubernetes Observability. I think there are some comments here. I don't know what the status is.
**Tiffany Hrabusa** 10:32 If I remember correctly, there were some notes, but then someone was on paternity leave.
**Dan Gomez Blanco** 10:37 Yeah, I think it was, alexandrik, I think, so… Kyle.
I think volunteer to… To continue.
I see that there is, Yeah, the scope… I think the scope has been agreed.
So… okay, so I think there's a comment here from Jake about… I'll have a… we do have a template now, so I think that's probably now asked of, This is an interesting one, I guess we'll… be interesting to discuss here. This is why it's good to have the scope, because currently there is, I guess, the best practice will soon change as the Kubernetes, Semantic conventions are stabilized, and then we could be using… KS cluster receiver, no KSM.
And that will be an important one.
to discuss, as a group.
Because I do believe that. Yeah.
We should be… A little bit opinionated, we can be, if we want, and a blueprint, it's, it's okay, so it's a point of view, it's just one way of doing it.
M… But yeah.
Makes sense.
Alright, so that's, yeah, that's for review, I think we're still probably gonna get some more comments, Kylie's not here, so probably… Yeah, not worth talking about it too much.
So, yeah, so I think, anything else that is… I think we have probably done this already, I'm just thinking, we have been doing this.
For the initial scope, we have decided to… cover… Mmm… We talked about Kubernetes, We talked about… non-Kubernetes environments, and we talked about centralized telemetry platforms, so I guess… This could be… marked as done. I think we have.
Agreed on the three blueprints that we want to cover.
Mmm…
**Tiffany Hrabusa** 13:14 Sounds good to me.
**Dan Gomez Blanco** 13:16 I'll make an update later, and call that as done.
On the missing… on the reference architectures piece, yeah, we can probably… talk about that next week. So, there's emerging topics here, because I was gonna talk about KubeCon later, but, there will be folks on the DevEx SIG.
But I, I keep calling, so I… Yeah, I think we should… have a chat together, see how they plan to… if they plan to have a… because I've read the blog post, the initial blog post that was pushed, and then, you know, if we're… if we're going to be asking folks to, hey, reach out to us.
To… if you want to share a reference architecture.
I think that process could be a little bit, more, I guess… Streamlined, in a way.
I mean, like, open an issue here, or whatever. At the moment, I think it's like, hey, reach out to us in the DevEx SIG, and maybe we can… we can just, have an issue template in the SIG and use a repo for that type of thing. But yeah, I guess… That will probably… they'll probably be helpful to have a, A reference architecture template, and so on.
Yeah, so these ones are, I guess, being discussed.
Mmm… But not currently being worked on, I guess.
And this one… well, I guess this one we can mark it as in progress, if we're talking about it now.
Which is… probably related to your point, maybe, I think, and that's, yeah, you wanted to see if we should start the architecture setup in .io.
Right.
**Tiffany Hrabusa** 15:06 Yeah, we'll need… I think the idea was to have some kind of explanation about what these are, so we will have to write some content, it won't just be, creating the pages. But I can get a start on that so that, when I think, Lukash is… Blueprint is probably the furthest along, and it might be… Are we intending to publish one at a time, or do we want to publish all three at once? I'm not sure, but…
**Dan Gomez Blanco** 15:37 I think we should publish one at a time, and…
**Tiffany Hrabusa** 15:40 Okay.
**Dan Gomez Blanco** 15:41 Yeah, thanks so much.
**Tiffany Hrabusa** 15:42 then, yeah, it might be worth, starting that, and I can, I can open a Google Doc that, for drafting the explanation. Unless you have something already written, Dan, maybe.
**Dan Gomez Blanco** 15:57 No, I think you can take, I guess, inspiration from the project, description, from the project template, if you want. Okay. But yeah, I think, Yeah. I guess, what do we want to cover? Like, we want to cover the… What do we mean by a reference architecture? What do we mean by a blueprint? And then… yeah.
And then inside, maybe… in each of, or maybe at the top, I'm not sure, whatever is easier.
how to propose one, but I think, you know, maybe that… that also needs… I guess there is an… there's an issue here to create, like, an issue template in the end user SIG.
Which… maybe, like, for now, we can just create that, and then we can add it later, too.
The process to create one.
**Tiffany Hrabusa** 16:50 Yeah, and if everything isn't ready.
in the explanations that we're putting on .io, we can hide the pages temporarily until we're ready to actually hit the button, but I think, It might… it might be a good idea to at least, Create the pages and get that started, but…
**Dan Gomez Blanco** 17:13 Yeah, I agree.
And then in the meantime, I mean, creating an issue template, it's fairly simple, right? So I can just create an issue template. I can focus on that first, before… And create an issue template on the… Say again, user repo.
I will create one, but maybe next, maybe, like, I just wanted to chat to the DevEx.
Folks first. Right.
**Tiffany Hrabusa** 17:38 I mean, none of this is gonna happen in the next day, so…
**Dan Gomez Blanco** 17:42 I mean, next week is KubeCon, right?
**Tiffany Hrabusa** 17:44 Yeah, yeah.
**Dan Gomez Blanco** 17:46 Yeah.
**Tiffany Hrabusa** 17:46 I'm on a plane tomorrow. You can assign 238 to me, and I will… take that on when I get back from the conference.
**Dan Gomez Blanco** 17:54 237.
**Tiffany Hrabusa** 17:57 238, the Blueprint section and guidance and website.
**Dan Gomez Blanco** 18:01 Right, okay, cool.
I guess that is.
**Tiffany Hrabusa** 18:09 Oh, I guess there's two things.
**Dan Gomez Blanco** 18:10 So there's a bit of an overlap here, right, because both of them would be under one. Right.
**Tiffany Hrabusa** 18:15 Right. Yeah, you can do both, yeah.
**Dan Gomez Blanco** 18:18 Yeah.
Yeah, I'll assign both to you, and then… yeah. So I think…
**Tiffany Hrabusa** 18:23 Yep.
**Dan Gomez Blanco** 18:23 They're almost, like, both can be done at the same time, I think, pretty much.
Hmm.
**Tiffany Hrabusa** 18:29 Yep.
**Dan Gomez Blanco** 18:35 Why is… why are people not? I don't know why. I can't really see.
People that are not commenting on that?
Do you need to comment on something to be able to… Second.
**Tiffany Hrabusa** 18:46 comment.
We'll test it right now. This… I'm on 238, so…
**Dan Gomez Blanco** 19:06 Nope.
Right, okay.
**Tiffany Hrabusa** 19:10 There we go. Let me do 2372. I might have already commented on 237.
**Dan Gomez Blanco** 19:17 Yeah, I think I have, yeah.
**Tiffany Hrabusa** 19:20 Yeah, I did. Okay.
**Dan Gomez Blanco** 19:23 Cool. Alright.
**Tiffany Hrabusa** 19:28 I'll get started on that after KoopCon, and, circle back with the PR.
**Dan Gomez Blanco** 19:40 Actually, we don't have the ticket to… I'll create Zahir as a draft so I don't forget. I'm going to create… Issue template.
Templates, I'll just do both of them.
for… Reverence architecture.
A blueprint, and… sick.
And user report.
I want to clear the draft.
There we go.
Right.
**lciukaj@splunk.com** 20:22 And this is Sukash, I joined a bit late, so sorry for that. So, I've seen that you reviewed my document on Google Doc, and I was reviewing that. So, I didn't have a chance to look into the comments yet, but I will get back to work on this, and I will incorporate it in the next version.
**Dan Gomez Blanco** 20:40 Cool. Sounds good. Yeah, I think, Yeah, let's go… I mean, we don't need to go through the comments now, but, like, I just hope… I just, Mentioned that here, so others can also have a look at it.
**lciukaj@splunk.com** 20:52 Yep.
Yeah, okay.
**Tiffany Hrabusa** 20:55 it a read-through for copy editing. I haven't looked at it yet, so… lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps about, like, opening PR, or we still, like, should continue working in the Google Doc now, as of now?
**Dan Gomez Blanco** 21:07 Yeah, so I guess, you know, there's… a little bit of a dependency change here, because, Tiffany's gonna be working on the, on creating the section, and open.
So after we've got that, you can open the… the PR directly under that section. Yeah.
**lciukaj@splunk.com** 21:24 Makes sense.
**Dan Gomez Blanco** 21:25 It will probably be after… KubeCon, right? Yeah.
**lciukaj@splunk.com** 21:29 Yeah.
**Dan Gomez Blanco** 21:30 after Cuba.
**lciukaj@splunk.com** 21:30 I'm not traveling, I'm not traveling, I'm not joining KubeCon this time, so… so maybe I will have some time next week working on this, so then we have a solid draft we can review, and maybe that will be ready for publish.
**Dan Gomez Blanco** 21:43 Nice.
What I would say is, as well, we… I'm not sure if you were here last meeting, we agreed on Mermaid for the… For diagrams, so yeah, if you were to… To add some diagrams in that.
That is probably the.
**lciukaj@splunk.com** 22:02 I think… I was thinking about including some high-level general diagrams for this, so, yeah, I don't have any experience with Mermaid, but I think it's kind of a straightforward tool, so I should be able to use it.
**Dan Gomez Blanco** 22:17 Yeah, cool.
**Tiffany Hrabusa** 22:18 Yeah.
**lciukaj@splunk.com** 22:19 Perfect.
You guys joining KubeCon next week?
**Dan Gomez Blanco** 22:22 Yeah.
**lciukaj@splunk.com** 22:23 Yeah, lucky you.
I submitted some proposals, but these were not approved, so without approved session, it's very difficult for me to get, you know, travel approval from my employer, too.
Hopefully, do you know where is the deadline, or is it already CFP open for KubeCon North America?
I haven't seen an announcement. I think it will be open soon.
**Dan Gomez Blanco** 22:53 It'll be open soon, yeah. It's always, like, earlier than I… than I want it to be. Every time I miss it.
**lciukaj@splunk.com** 23:02 Maybe we can, you know, submit something jointly for Observability Day that is related to Blueprints. Hopefully by this time, we'll have, like, this success in this project, so maybe we can share that with the entire community.
**Dan Gomez Blanco** 23:17 Yep.
I think it would be good. I think it would be good to maybe, yeah, talk about… There is a little bit of, I guess… For anyone that is in a solutions architecture, or, like, basically.
**lciukaj@splunk.com** 23:34 Works.
**Dan Gomez Blanco** 23:35 in this field. I think that it's, like.
The understanding of what a blueprint is, compared to, like, hey, here's a list of Here's a, here's a user manual, right?
**Tiffany Hrabusa** 23:47 you know.
**Dan Gomez Blanco** 23:47 And then, yeah, sometimes it's not super understood what we mean by a blueprint, for example, right? So, I talk about that and the benefits that it can bring to the community would be… would be quite good.
Yeah.
I mean, that would be… Yeah, be happy to… to co-speak, if you… if you're willing to.
**lciukaj@splunk.com** 24:08 Yeah, let's, let's work on that. But first, let's have a PR, and first…
**Dan Gomez Blanco** 24:13 No, I mean, firstly.
**lciukaj@splunk.com** 24:14 Yeah, that is real, we are…
**Dan Gomez Blanco** 24:16 Point and stuff.
**lciukaj@splunk.com** 24:17 Exactly, so then we will be in this real phase instead of, you know, pre… pre-GA, let's say. Let's make this GA, right? So I assume first blueprint will be… will be the GA for the project, so let's work on this.
Awesome.
**Dan Gomez Blanco** 24:32 Sorry, I was just reading the chat, welcome, Gloria.
**Gloria** 24:36 Hi, thank you. Sorry, I didn't mean to interrupt, I'm just kind of observing, but yeah, I, Andre, at the behest of Andre, I'm… want to get more involved, and see how it can help out, so… Awesome. Thank you all.
**Tiffany Hrabusa** 24:52 Yeah, we're happy to have you.
**Dan Gomez Blanco** 24:54 Exactly. So if you want to read more about, you know, blueprints, part of the End User SIG, if you come to this, you will see the notes, I'll drop the notes in there. The… the, definition of a project is here as well, the full README, if you want to read more about what we're trying to achieve, if you click on this, on this link, what we're trying to achieve with Blueprints, what are the deliverables, and… And then, yeah.
One thing that I wanted to talk about with folks is that when… with your… originally, we… created this project proposal in December, but we didn't really start Mmm… well, January 9th is when we started, and originally, you know, we put this as the target date, but this is open source, and I think, you know, we are not… yeah, we're not held accountable for this target date. So clearly, this is a bit too optimistic, But I was thinking that, looking at the current progress, if we can give an up… I mean, this is something that, I guess, one of the things that… Just put in my… Governance Committee Emeritus hat on is something that we're… we're always trying to… Like, be better at communicating progress.
on initiatives?
And this is something that is… people just want to know, hey, you know.
how… how are you doing? How is it going? And what are you… so if we… if we think… that we can maybe achieve this by, I don't know, the end of June? Or we can have those 3 blueprints.
I think calling it end of June, for example, would be doable, because we've got The three blueprints that we want to have in progress.
We have reference architectures that can be published.
But they are… I think there's only one missing. I think we were calling out for 5, and I think the DevEx SIG already has 4, sort of, ready to go.
So if we say… you know, 30th of June.
What do others think? Is that, like… A good, like… I don't think this will… basically, what I'm trying to work out here in quarters, rather than, like, you know… I don't think this will go into October, I think, hopefully.
So yeah.
**Tiffany Hrabusa** 27:17 I think end of June sounds reasonable.
**Dan Gomez Blanco** 27:24 So I'll just give an update, and see.
Okay, Blueprint Brewery.
3, 3.
Alright, so let's give an update, and then people will be able to get this in the hotel… roadmap.
Which… If you… Come here… It's not pinged.
Actually there's… should be in the projects.
the OpenTel integer roadmap.
Right. This will take some time to… Update, but it will show up here.
As you can see, yeah, some of the… some of the projects were also very optimistic. It's quite a normal, so… Yeah, it's a no-tail thing, we're all optimistic, and how long it's gonna take.
Okay, so, yeah, so I think we talked about KubeCon EU, and we're gonna have a… A special slot, and we're near the project pavilion.
I think we can pro- I'll probably share some details in our… in our group.
And then… posted online at some point or something. I think, you know, if we can get end users to participate.
I guess my question here is, like, what would you like to… what would you like us to focus on if we get end users that want to join?
Would we want them to come and review the blueprints that are covering in progress? I guess that's… That would be one big win, right?
**lciukaj@splunk.com** 29:53 Or maybe suggest the new blueprints as well, right?
Yep.
That'll be good. If you have a chance to talk to end users, maybe try to… Get some insights from them, hey, what is currently being missed, or something like that.
**Dan Gomez Blanco** 30:08 Yep.
Yeah, makes sense.
And then, the chat with the DevEx.
sake as well.
About how we… how we can better collaborate there.
**lciukaj@splunk.com** 30:24 Alright guys, I need to jump to a customer call. Enjoy CubeCon. That's alright. Two weeks.
Good to see you.
**Dan Gomez Blanco** 30:31 Yeah, with that, anything else?
I think we are… We've covered everything.
Good stuff. Alright, well, See you in Amsterdam, Tiffany. Yep. And are you gonna be at the Maintainers Summit?
**Tiffany Hrabusa** 30:50 I am, I'm speaking on a panel of documentarians, so…
**Dan Gomez Blanco** 30:54 Nice.
**Tiffany Hrabusa** 30:55 Yeah.
**Dan Gomez Blanco** 30:55 I'll be there.
Okay, well, thanks all for joining, thanks Clara, for joining as well, and welcome, and, see you in two weeks.
Oh, by the way, Gloria, in case you were wondering.
**there is no ups… there is not going to be any end-user SEG meeting next week, I believe. You know, most meetings in hotel tend to be canceled during Qubicon, because everyone's away, so I think they… Gloria** 31:20 Yeah, Andre mentioned that to me, so I'm probably gonna use that time to… Look into the documentation a little bit, and get up to speed.
**Dan Gomez Blanco** 31:31 Cool, awesome. Alright. Great. We'll see you in two weeks.
Bye.
