SIG: GenAI SIG
Date: 2026-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:02:57 Hello, hi everyone.
Surya Teja 00:03:01 folks.
Jeff Leva 00:03:03 Good morning.
Victor  Lu 00:03:33 I think last week, I left, just sharing that, taxonomy document.
If there's interest, I can continue today.
Liudmila Molkova 00:03:50 Oh, yes, please do.
Pam Dixon 00:03:58 This is Pam. I still have a raised hand from yesterday, or excuse me, last week. Time is flying.
Trask Stalnaker (Microsoft Corporation) 00:04:06 Alright, let's get you on the agenda.
What was your… Topic…
Pam Dixon 00:04:16 Yes, thanks. My topic was responding to the identity definition proposal, as I'm looking at my notes here.
Yeah. So, last week's question was whether the… some of the attributes could be, you know, made the same. So, I actually took some time to look at that a little more closely and have a response.
Trask Stalnaker (Microsoft Corporation) 00:04:59 Cool! We can kick off with your… Findings?
Could you maybe reframe for those of us with short-term memory, the big, bigger picture here?
Pam Dixon 00:05:13 Actually, if… if Victor could do that, that would be really helpful. He proposed a, kind of a… he made a proposal, so that's what I'm working from. So, That should probably come first.
Victor  Lu 00:05:30 Yeah, I can, I can go, go first.
Trask Stalnaker (Microsoft Corporation) 00:05:37 Cool.
Victor  Lu 00:05:41 So, well, you wanna, you want to open my, the document I put in the chat?
Trask Stalnaker (Microsoft Corporation) 00:05:50 Oh, sure.
And if you would prefer to share, that's fine also.
Victor  Lu 00:05:59 Yeah, so this is, really, at this point, a start to, the reason… this actually started a discussion in the, OpenID Foundation, where there's a AIM, Agentic AI working, working group there.
So, it's understood that there are a lot of, different, opinions about the definitions, especially the agent identity and agent credential. Especially agent identity, there's a lot of different opinions on what it should be.
So, actually, it looks like there are actually a couple comments already, added to this, document, but it looks like they're not showing, from your, screen. So, yeah, so, the,
Trask Stalnaker (Microsoft Corporation) 00:06:54 Would you like to share, Victor?
Victor  Lu 00:06:56 Sure, sure, maybe I can share it better. I show some on my screen here.
Yeah. So, then I discuss in the, in that community and say, there's a lot of different agreements, so it's necessary to, Yeah, you can see now, right? So… Yeah.
And then, so… I took it to multiple communities, and then, I think at this point.
The definition itself is one thing, but really, this is very useful to make the two telemetry, if you will, the community that's being hotel and OCSF to be in sync. So this is really a vehicle for… for that purpose, mainly, at this point.
So, I took the first definition, which comes from OCSF, So, and then down here, in appendix, I added some additional information, given by the, OCSF community on how they make conclusion on that definition.
So… Be aware this definition at this point is work in progress, and that this definition here, may not be… may still be kind of a, influenced by the previous work, of OCSF, which was a security, CM, schema, right? So, but, yeah, so that's where it comes from.
Then, this one.
is different. This is really an opinionated definition from COSI community. If we're not aware of what a COSI is.
it is a community, really, of most of the major, you could say the AI players, you know, OpenAI, Anthropic, Cohere, and a whole bunch, you know, Google, Microsoft, Cisco, everybody is there.
So, so this is a very opinionated, definition, whereas this one represents OCSF's, current definition. Yeah, so is this really just a starting point? so, yeah.
Liudmila Molkova 00:09:09 Can I ask a quick question?
Victor  Lu 00:09:10 Yep.
Liudmila Molkova 00:09:12 It sounds like there's two things… these are independent things, right? It's not… Two different definitions of the same thing.
Victor  Lu 00:09:20 It is… what do you mean, it is… it's a definition given by OCSF at this point. They're willing to, you know, open to change it.
Liudmila Molkova 00:09:32 Oh, no, I'm… I'm saying the Agent Identity and Agent Credential are two independent things.
Cure.
Victor  Lu 00:09:41 That's actually, if you look at the comment, the… Let me see… Hold on one second, let me, un… Give me one second, let me change a little bit here, sorry, let me actually… Make it bigger… Here… Okay.
So… Let me make that, comment more visible.
You can see the comment now, right? So… So, they're, they're actually, There is, already been pointed out, there's a difference between identity and identifier, and, so, Yeah, so there's definitely some different opinion about it already, and that seems to be common. At first, I thought it was a… more of a, you know, decentralized identity community thing, but it turned out both the centralized identity, that's the, you know, the OpenID people and decentralized people, it seems to have the same opinion. So that definitely, needs to be adjusted.
Again, this is the first version.
Liudmila Molkova 00:11:01 But, like, I… Is… is… so what you're saying, there are different opinions there?
Seems they're aligned on identity and identifier being different things.
Victor  Lu 00:11:14 No, identifier, Identify… I mean, so, so, actually, it was discussed whether When we're focusing on agent identity, there's an opinion saying, instead of talking about agent identity, it should be agent identifier.
Liudmila Molkova 00:11:32 Oh, it should be probably both, right? Both are interesting. That's what I'm saying.
Victor  Lu 00:11:36 Speaking.
Liudmila Molkova 00:11:36 to ask if…
Victor  Lu 00:11:37 Yeah, could be, yeah. Maybe I should replace the agent skill with agent identity as the third most important concept to be defined.
Liudmila Molkova 00:11:48 Yeah, okay, thank you.
Victor  Lu 00:11:50 You're welcome.
Yeah, so, again, this is only starting…
Liudmila Molkova 00:11:53 Pam Hase has.
Victor  Lu 00:11:55 Yeah, Pam, yeah, go ahead.
Pam Dixon 00:11:58 Yeah, hi. So, I've worked in identity about 30 years at really detailed and hyperscale levels. I worked on Adhar in India for about 10 years. So, look, telemetry is not identity, it's different. And that's part of the reason I'm here, because it's incredibly important to understand the differences. So, I'm in ITUT, SG17, where I work on Agentic identity standards, as well as quantum standards in relationship to AI quantum harnessing.
So, one thing I can tell you, that… and I think that it might be the crux of the kind of the definitional difficulties that, that, are here right now. So, we're really talking about two things.
under one word, and I think that's really the crux of the problem. So, when you're talking about telemetry, the agent identifier is actually a grouping label. This is my understanding, and I might be wrong, so please, please correct me.
Trask, etc, Ludma, but, it's for the hosted agent resource. So, the proposed identity you're really talking about is a credential-based item, and it's meant to converge across observers. So, if this were to become the definition.
in telemetry, it would change the meaning of the existing, I believe it's now 3 items, there might be more, that relate to, identity. So, my understanding is that merging these ideas would make every existing value for identity read as an authenticated identity, in essence, and then the related entries for that telemetry would then depend on each other in a very hard way. So, I would propose that these should be kept quite separate. So I guess my question to you… Is the, you know, what use case Would require that one identifier be joined across runs.
and across observers, within the telemetry record, because that's really… that's really what these definitions are going after. So I think it's just really important to keep these items quite separate, and again, Please, please, for those of you who have been in telemetry a lot longer than me, please let me know if I've interpreted this incorrectly, but in terms of identity, credential-based is really different than what telemetry is doing, is my understanding. Thank you, that's it.
Trask Stalnaker (Microsoft Corporation) 00:14:44 Yeah, I would say we have, in OpenTelemetry and Symmetric inventions, we've done very little with authenticated identity, or tried to differentiate those.
So yeah, our… Our general… Use, usage of the term agent identity, or identity.
Has been, as you described, it's like the thing that you want to group on, it's the thing that is interesting from a telemetry perspective to group Bye.
Liudmila Molkova 00:15:26 It's also interesting to include the, let's say, spiffy ID on the telemetry. One does not prevent another.
Pam Dixon 00:15:35 Yeah, and I think just from my initial understanding of how the architecture works, that makes sense, and it really makes sense for telemetry to remain as it is, as a grouping.
when you… when you think about the infrastructure of how telemetry's working across, you know, tool calls and spans and traces and across jurisdictions, I mean.
from my read of telemetry, I mean, it's… this is going to cross jurisdictions all over the place, from one country to another, and if it's geospatial, it'll have a different governance mechanism. I mean, to tie this to a certificate-based identity would be… profoundly difficult, and I just… I think it kind of defies the purposes of the… of the telemetry use of ID as it is right now. That's just my take. Thanks.
Liudmila Molkova 00:16:30 And from telemetry perspective, we… we would take as a stable identifier anything that system considers to be a stable identifier.
If, for a semagentic system, They use their identity I… Like, something like PPID for this purposes, something related to credentials.
That's totally fine, we don't care.
But it's also interesting to say, oh, what How my agent was authenticated.
And this is, like, orthogonal problem for us in telemetry.
Pam Dixon 00:17:17 Yeah, that's a hard problem, for sure.
I think there might be… I'm really… this is the question I, came with you… came to you guys with originally, trying to see if maybe a field designated as provenance of authority, or just relationship to authority, not authentication.
And I don't know the answer yet. It's a really, really hard problem, but I… I think that having a kind of a local ID is a very reasonable thing, and it sits with all the other identity, terms that are already, defined within telemetry. It seems reasonable.
Trask Stalnaker (Microsoft Corporation) 00:17:58 Potentially to help scope the discussion, So, what we're generally in… trying to do from semantic conventions is, give a place to put things that are already capturable.
Like, we're not trying to tell agents, hey, you need to rework your whole infrastructure, your whole everything, in order to produce XYZ, We are… I mean, that is a great problem. I think that maybe that's… but that's way broader, and I think that… might be sort of what, like, the COSI and or AAIF, groups are… Taking that bigger picture there of trying to drive changes throughout the agent.
For us, We're more looking at, hey.
more concrete, like, what are the things that are already available? That some agents… now, not all agents have to have it available, but if some agents, you know, more than one, we require, generally, like, we're like, if there's something that's reasonably common for… that agents have available, a data point.
Then we would consider, okay, how can we standardize what to record that as?
Pam Dixon 00:19:25 Yeah, I think that's… I think that's the right way to go.
Victor  Lu 00:19:31 Thank you for the input, Pam. Actually, this is, as Trask already said, that there is already a collaboration, I think, between OCSF and OTEL slash COSI when it comes to overall metrics for Agentic AI.
These three terms, actually, I should say two terms, agent identity, agent credential, not probably, as you said, I think, since the agent identifier should be the third important one to replace agent skill definition to be discussed.
This is a very hard problem to be… concept to be defined. This is, at this point, beyond the original scope for the OCSF Hotel, Okosai collaboration. That's why I'm taking it to beyond that.
boundary. This is being shared in… Itu is good. It's good that you actually… because I don't know how to reach out to ITU, because, before this, I really reached out to W3C, IEEE, ISO, Open IT Foundation, and diff… Iaif, of course, OCSF, COSI, and probably more.
So pretty much everybody who… every community that could potentially be talking about this topic is… is reached… reached, contact at this point.
So, it won't be so simple. Hopefully, somebody else actually can take it over at one point, and at one community can talk about it. But at this point, this is mainly, the home of this is in the OpenID Foundation, AIM Taxonomy Working Group. That's the current home for this, at this point.
Pam Dixon 00:21:14 So, OpenID Foundation is working with ITU on multiagentic identity, but I'm just going to, again, say what I already said.
with apologies. I think that you're using the term identity in a really different way than is defined in the semantic conventions, at least the ones that I've read. And I think that that's probably the source of the conflict.
And I would just encourage you to look at that, because telemetry is just a really different ball of wax than what OpenID Foundation is working on, and even ITU. Some of it touches telemetry, but where it touches telemetry, people usually allow the telemetry to have its own definitions.
For a lot of good reasons. So I would encourage you to, you know, reach out to the chair of STU, ITU SG17, To kind of see what… what's happening there. There's an in-person meeting in Paris, next week. So, it would be a good time. But the, the, the definitions in terms of, what I call hard ID, Where you're actually, you know, certifying. That… that is in motion.
It's in motion, but it's agreed that it's a profoundly different thing, and it's also agreed that it's different than telemetry.
Thanks.
Victor  Lu 00:22:43 If you can, maybe… maybe that's my email, if you can maybe share that contact, that would be great. Definitely love to be in sync with everyone. The problem is ITU, similar to IETF, right? It's not… there's no regular meeting. At my understanding, there's no regular meeting.
So I'm reaching out to communities where there is a regular meeting, so I, you know, there can be, you know, continuously to be discussed, rather than just, you know, wait I have one meeting and wait for 3 months for the next meeting, which is impossible to have a consistency there.
Pam Dixon 00:23:11 Oh, no, there's very regular meetings. So, if you put your email in the chat, I'll reach back to you with this, so we don't take any more time.
Victor  Lu 00:23:21 earlier this, having my email in the chat, yeah. So on the right-hand side, if you can see… thank you, Pam. This is actually a definition suggested by another, by, But Peter, he is in the, I think he's either in the MCP community or in the, the IAF community. He gave this definition. So, this is actually… this definition come, no, actually, the original, this one comes from OCSF.
So, I think they would… I'll take this feedback, and so I think, for sure.
the three concepts that need to be defined in that case is replacing agent skill with agent identifier. So the agent identity, agent credential, agent identifier that need to be defined.
And again, I think at this point, the actual definition is hard, but I think at this point, the more practical goal is to make, you know, OTEL and OCSF to be, you know, in sync on these concepts.
Yeah, yeah.
Liudmila Molkova 00:24:18 It seems we do have a concept for the identifier today in semantic conventions. I just posted a commenter's link, and let me post a link in the chat as well.
We call it GenAI Agent ID, and this is the stable logical Identifier for the agent. I think this… this fits perfectly.
So whoever decides what goes into this ID, we would happily support them, and we would work with them, could… we aligned on the attribute name, and… or could COSI just say that, okay, define the thing, and say this is how it's captured to not tell? Would it be something we can, like.
work towards.
Victor  Lu 00:25:02 I will share that with the OCSF team, so that they understand the overall feedback on the concept, as well as the current definition from OOTEL. This way, you know, how to… I mean, obviously, it's not so possible to change everything, existing definition, but probably, yeah, how to map it properly is probably the question.
Liudmila Molkova 00:25:23 Okay, so that OCSF-defined… okay, yeah, OCSF defines attributes, makes sense, okay.
Victor  Lu 00:25:31 That's, that's the current creation. Again, this is the first version. Definitely, it's good that we already replaced the definition, replaced agent skill with agent identifier. That seems to be the… nobody seems to have any, like, disagreement of an agent skill. Also, maybe not as important, so I'll probably replace that as the next version, if you will.
Liudmila Molkova 00:25:52 Awesome.
Victor  Lu 00:25:53 Thanks, that's all I have.
Other comments?
Well, actually, I do have one question. I don't know… because I usually, usually is… I usually take other people's… use other people's documents, but this time, I'm actually creating one shared by… I mean, many people. How do I… how do I make people see the comment without actually giving everybody a global, comment access. Is it possible?
Liudmila Molkova 00:26:29 I don't know.
Trask Stalnaker (Microsoft Corporation) 00:26:30 I don't know.
Victor  Lu 00:26:31 I'll try to figure out, yeah.
Thanks.
Liudmila Molkova 00:26:36 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:26:44 Alright, moving on, Ludmila, what…
Liudmila Molkova 00:26:48 Before we go there.
Trask Stalnaker (Microsoft Corporation) 00:26:49 Oh, yes, sure.
Liudmila Molkova 00:26:50 There was a topic next from Jeff Leva above, about the COSI VS2.
Jeff Leva 00:26:58 Yeah, hi, I'm here.
Liudmila Molkova 00:27:01 Oh.
Jeff Leva 00:27:02 Yeah.
Liudmila Molkova 00:27:03 Oh, I moved it under Victor's topic, sorry.
Jeff Leva 00:27:05 Oh, it's okay.
So I just provided… last time I spoke to you guys, you wanted a global… or not a global, but a higher… overall issue that COSI, wanted to present to the group. So this is that document, kind of giving you the 10,000-foot view of some of COSI's objectives, and then… Drilling back down into some of the, attributes that we wanted to get some definitions in line with your, your, hotel, specs, so… I don't think you guys probably not had a time to look at this issue yet, so… Basically, this is just awareness that it's here.
Give you a chance to review it.
Trask Stalnaker (Microsoft Corporation) 00:28:05 memory…
Liudmila Molkova 00:28:14 Quick question, and sorry if you already answered it in the text.
Where would the information… Come from the new… Attributes, things like the trigger type, trigger event.
Who would send them when and how.
Jeff Leva 00:28:30 Oh, we would provide, I mean… I think because last time we talked, it was like, you know, there… It depends on what we're trying to accomplish. It could go into different work streams for hotel.
And… So, I mean… We would provide what we would need as topics, and then you guys could tell us where to discuss them, and…
Liudmila Molkova 00:28:54 Oh, no, no, I'm, like, from the… let's say we want to implement it.
Where the implementation of this data collection would leave.
Jeff Leva 00:29:06 Well, I think, again, the goal is to, maybe I'm not understanding the question, but, like, to get synced up with you, so we would have… Our data live in COSI.
Liudmila Molkova 00:29:23 So we… Have the conventions, but our goal is to have the instrumentations that can collect the data.
And, It can be done by… from the libraries, like, I don't know, Entropic client, from the frameworks, or from harnesses, from applications.
But we usually try to, like.
Model things end-to-end, and see how the data can be collected.
Jeff Leva 00:29:56 Yeah.
Liudmila Molkova 00:29:56 Before we define something, because if it's not collectible, then we have a hard time defining it.
Jeff Leva 00:30:05 precisely.
Liudmila Molkova 00:30:06 enough.
Jeff Leva 00:30:07 Yeah, I think the other part, too, is, you know, I work with Victor, too, with the OCSF team, and so the overall goal is to have alignment as far as we can.
And we can certainly work on data collection on where it lives, and…
Trask Stalnaker (Microsoft Corporation) 00:30:26 So this is kind of, yeah, what the reference scenario here is getting at is… and you can see how the other semantic conventions in this repo have, sort of, reference scenarios against Different… libraries to show, you know, what are these mappings? Kind of back to the earlier discussion, right, we're… we're not trying… our… our… we… There's such a huge possible scope of this work that we try to keep it… there's already too much just within the more narrow scope of how do we map existing things that people are already That are already capturable.
Jeff Leva 00:31:13 Gotcha.
Trask Stalnaker (Microsoft Corporation) 00:31:14 And so, you know, if, for example, you're trying to propose this, you know, more, like, as an industry standard that you want libraries to adopt.
That's maybe a different avenue… Possibly, like, we kind of… at this point, at least, we're kind of taking what libraries… we're just trying to keep up with what libraries are already capturing And have a place to put that information.
Jeff Leva 00:31:44 Gotcha.
Trask Stalnaker (Microsoft Corporation) 00:31:54 Yeah, thanks for opening this, you know.
helps to get a sense of where you're going. Yeah, and then… for the… yeah, I think that the PR is helpful also for kind of looking at something concrete, and if you can kind of think of what reference scenarios would exist for that. Other possible, like, scenarios could be, like.
maybe it's a collector, receiver, for example, kind of a thing. Sometimes things are not capturable via traditional instrumentation, but they are capturable via, like, scraping something from a collector receiver, and so… That could be a prototype. For example, you could send a PR to Collector Contrib to show, like, what a prototype for that would look like.
Jeff Leva 00:32:48 Okay, so would you guys not… I mean, are you still gonna review this?
Like, would you put comments on this issue? Or is this basically what it gets? It's just a little… I mean, because it's better for me if things are documented, then I can… follow up and do what needs to be done. So, I mean, I can take the feedback now, but… Does that mean you're not gonna, like, really review the issue and leave notes, or is this… Just did.
Trask Stalnaker (Microsoft Corporation) 00:33:18 When we have time, we've got kind of a large backlog that we try to keep up with, so that's where this meeting is helpful for people who want to, like, sort of get some immediate feedback.
Jeff Leva 00:33:31 Okay, alright.
Okay, well, I'll take the feedback and…
Victor  Lu 00:33:35 One thing that was discussed in the COSI meeting is about forming an actual hotel security review, or whatever that is, group. Trask, do you think that's a… even if it's not formal, do you think that's a possibility?
Trask Stalnaker (Microsoft Corporation) 00:33:54 Sorry, like, a general security, semantic convention security, or…
Victor  Lu 00:34:01 Specific.
Trask Stalnaker (Microsoft Corporation) 00:34:02 GenAI security, like, a breakout?
Victor  Lu 00:34:05 Yeah, probably a GenAI security, because at this point, it's more security. If you look at the OCSF schema.
it go beyond just GenAI security. In many security scenarios, the two cannot be separated. You cannot go AI security without general security, non-AI security.
But at this point, it's focusing on GenAI security, so probably start with that, and maybe extend… after finishing some initial foundation of that, can probably think of how to extend GenAI security to cover all security.
Trask Stalnaker (Microsoft Corporation) 00:34:49 So this… I mean, is there a… Benefit to that being under the OpenTelemetry umbrella versus under the, I mean, the COSI… or OCSF.
umbrellas…
Victor  Lu 00:35:10 Yeah, that can be flexible. For example.
If you think there's no need to set up a searching here.
you can nominate COSI to be the de facto, if that… if people agree on that. You know, I know other communities also like to participate, and not part of COSI.
But if everybody agreed that's a good idea, I can nominate COSI to be the de facto review community. Kind of a preview for… to be before it's being presented here.
The reason for that is, security is very kind of a closed-loop, topic sometimes.
For example, there's a lot of things that cannot be achieved just by adding one metrics. It really is kind of a… need a lot of additional, information to be useful.
I don't know that… I don't know if that's a proper way to describe it, but Jeff, do you have any other thoughts about that?
Jeff Leva 00:36:10 Oh, I think what you said is accurate, yeah. I think… That's about right, how I would see it.
Victor  Lu 00:36:16 Thanks, the pen.
Pam Dixon 00:36:21 Yeah, hi. So, I have… obviously, I… it's not for me to say, but if a security subgroup, does form, could it work, then, under the same scope, that has been generally talked about here, which is… that it's reference scenarios against existing libraries, with open meetings on the calendar and notes provided, but references against existing libraries. Thanks.
Trask Stalnaker (Microsoft Corporation) 00:36:51 Yeah, I mean, that's a good point that, I mean, generally that is the… I think that's the scope that… we could… tackle if you… yeah, so I guess it kind of depends on what your… goals are at this point, Victor and Jeff.
I know we have, Ludmila and I have, five, GenAI, meetings a week.
Already on the calendar, so, you know, it's kind of pushing our, limits to add more, Meetings.
But there's definitely, you know, one way to kind of gauge interest in the community is to, you know, open a community issue or a, proposal for, you know, a new SIG, essentially, a new project here.
and, you know, see if we get enough interest and, you know, to support that.
But that's sort of where, you know, like, I feel like if you'll have, the OpenTelemetry community is great when, you know, we have multiple vendors, and there's not sort of, like, a vendor-neutral safe space to work in, then, but… Since you already have that within COSI and or OCSF, And since you already have people.
in those communities who are sort of the target, probably the target… most… the target audience for those. It could work well just to… Focus.
in there.
Yeah, Li.
Liudmila Molkova 00:38:47 Victor, if you want to reply, go ahead.
Victor  Lu 00:38:50 Yeah, I just shared a OCSF schema. You can see most of the current schema, all of this has security.
And AI is just a very small portion of it. So, definitely, I think in the short term, it's having the… COSI slash OCSF collaboration, like Jeff Lee is proposing, is probably the best way, because that's where the expertise are right now. But the, the thing is, some… some people, some of the organizations want to adopt, like, a mix of hotel slash OCSF for their solution.
There are actually many companies who want to adopt a kind of a hotel-only solution, actually.
Whether that's feasible or not, that's a different story. So that's why I think there's interest, for sure, after we establish an initial, the, the common matrix adopted by both OTL and OCSF.
there might be interest to say, you know, if we don't want a full feature, like CM, that's what SIEM, the OCSF, bring to the table.
maybe we need, like, a small subset of that for people who want to just do it on the hotel-only side. That's where I think eventually there is probably a need for a hotel-focused group that's outside of the the current, OCSF, community.
Liudmila Molkova 00:40:23 Yeah, I was thinking that… A lot of the things in Jeff Suchio is something that instrumentations can collect, and should probably collect.
Not all of them, but… things like the run or step ID, or things like the tool definitions hash, and many of these things.
And we cannot have… to external to OpenTelemetry. Well, we can… it can happen that there is an external to OpenTelemetry group that defines those, but it's very unfortunate because then we have… Some conflicts very likely to happen.
So for things that are collectible.
I think we have to work together.
But for the… things like the trust level, I don't know where we would get this.
from… On Atel's side.
And maybe… well, if I… if I had a magic wand, I would say that maybe OICSF and other communities provide the instrumentations or some components for OpenTelemetry that collect them.
But that's me being up in telemetry-focused here.
Jeff Leva 00:41:47 Yeah, I think that's possible. Sorry, Trask. I do have… I mean, that's kind of what I've done with OCSF, is I have a platform where I can run most of this.
data and show the JSONs and provide… Examples and house the data, so… it's not out of the question that we can do it that way.
Go ahead, Trask.
Trask Stalnaker (Microsoft Corporation) 00:42:11 Yeah, yeah, and I think that the… it sounds like the COSI… group is sort of working on defining these things and wanting to bring, sort of, land, the definitions in this repo, and I do think that, you know, as long as… as long as they are backed by Real instrumentations, whether it's instrumenting libraries or potentially, you know, collector, Receivers kind of a thing that, you know, we can… We should be able to support.
that.
Jeff Leva 00:42:51 Okay, yeah, that sounds good, because, yeah, we… we've got the part of this project, too, like, a lot of the OCSF stuff that… PRs that we've implemented came from a working platform, and then that turned into an open source tool in IBM Red Hat's Praxis repo. They have what we call an OCSF emitter, plug-in, and so, yeah, a lot of this can be… I mean, I can tool things to make it captured, and real evidence, too, in, like, in a working implementation, so that's definitely doable.
Trask Stalnaker (Microsoft Corporation) 00:43:28 Yeah, that would be awesome.
Jeff Leva 00:43:29 Okay.
Trask Stalnaker (Microsoft Corporation) 00:43:29 Yeah, I think that would really help us. We really look, because we don't have… yeah, we've found that really… helps us to move the actually land semantic conventions is to be able to.
Jeff Leva 00:43:41 Right.
Trask Stalnaker (Microsoft Corporation) 00:43:42 real. Exactly.
Jeff Leva 00:43:43 Exactly. And that's what we have to present to OCSF. It can't just be ambiguous. Take my word for it, this is, you know… So, yeah, I got you. Understood. So, yeah, I can work on that part, too.
Trask Stalnaker (Microsoft Corporation) 00:43:57 Cool! Alright. Sounds like we have a plan.
Jeff Leva 00:44:00 Yeah, okay. Thank you. I appreciate it.
Trask Stalnaker (Microsoft Corporation) 00:44:03 Yeah, and thanks for… yeah, and this, this meeting is a, you know, a great place to, for you all to come and, you know, wear, like, as much stuff as you all work out, once you kind of have agreement amongst yourselves, and then bring, you know, proposals here, I think that works.
Jeff Leva 00:44:22 Okay, sounds good. Thanks for your time.
Liudmila Molkova 00:44:25 Thank you.
Jeff Leva 00:44:26 Thanks.
Trask Stalnaker (Microsoft Corporation) 00:44:32 Alright.
Message parts.
Liudmila Molkova 00:44:36 Yeah… Okay, so… I… was working on something, and I realized that In the current language of the spec, we are saying to collect parts we don't know.
So, as we convert, let's say, input messages or output messages into semantic conventions, We are saying to… just… Give it some part name that's provider-specific, and put whatever part representation is into… An object?
And I have concerns about the stability. It's… there's nothing that… Guarantee stability, or… It even be in the language agnostic representation.
It's just a blob of… Something.
I thought… in my head that we are saying the opposite, to not collect them. So I send a PR, But I've got the feedback from Alex, the blocky one, that Having some telemetry is better than not telemetry at all, and I can see this point of view, that if we don't collect, we just drop some parts without ever saying they were there.
It could be confusing, you cannot debug it properly.
So, I didn't have a lot of time to think about it, because I just noticed Alex posted this before this call.
And… I want to… Kind of brainstorm what can we do?
If we collect them, how can we annotate them in the way to… so people know they are… evolve, they are going to evolve. We are not providing any Any backward compatibility for this?
These parts of the parts.
Trask Stalnaker (Microsoft Corporation) 00:46:58 Do we know the… list of parts? Like, when we're instrumenting, say, the reference note, or when we're instrumenting, do we know the list of parts, or is it dynamic?
Based on what the, provider returns.
Liudmila Molkova 00:47:18 Do we know the list of semantic convention ports? Yes, do we know the list?
Trask Stalnaker (Microsoft Corporation) 00:47:24 Go ahead, sorry.
Liudmila Molkova 00:47:26 Do we know the list of provider parts?
Maybe, but it's a very long list, and we don't… We don't know if the latest version doesn't have something new.
So, yes, in runtime.
Trask Stalnaker (Microsoft Corporation) 00:47:46 And there's a lot of them.
Liudmila Molkova 00:47:48 a lot. Like, I think on the call yesterday, I showed a list for the OpenAI responses, and it was, I don't know, a couple of pages long.
And they add them all the time.
And I don't think we will ever be able to keep up with all the parts of all the providers, and we shouldn't.
Trask Stalnaker (Microsoft Corporation) 00:48:12 So, things like, I mean, the… the schema of… Input messages, output messages, Is… there's already basically a… And any value in there for the part, like, the parts have… a type.
And then, essentially, an any value? Is that… Right?
Liudmila Molkova 00:48:41 Yeah, yeah.
Trask Stalnaker (Microsoft Corporation) 00:48:43 So, I mean, we're… we're already… there's not really… Any compatibility?
Guarantee there?
the… the part… That any value could change at any time?
Liudmila Molkova 00:48:57 Well, the any value can't change.
But we describe this any value to a certain extent.
And… in my mind, If we say… So we're saying that part has a discriminator, right, and whatever bag of properties.
And then, for this discriminator, these properties should be expected, and we support an arbitrary other ones.
If we are saying, that some parts are undocumented.
And our… Different across languages.
I kinda feel, why do we even try to normalize them? Let's just capture whatever providers have.
It's just any value, no guarantees provided.
Yeah.
Aaron Abbott (Google LLC) 00:50:02 Yeah, I know we've talked about the normalize, like, not normalizing thing before. Before we get into that, maybe, I was wondering, like, so we do have the… the text that says to do a vendor prefix, which you can have an example of here of the non-normative example with Anthropic. So that is in the spec.
Would it work if we just call out that Anything that has a vendor prefix is not Like, part of the stability guarantees of the semantic conventions.
Liudmila Molkova 00:50:34 Well, but it's totally valid for Anthropic to say this is our unique part.
And we want to document it and provide stability guarantees for this.
Aaron Abbott (Google LLC) 00:50:48 Yep.
Liudmila Molkova 00:50:49 And, like, what is the vendor prefix? Like, on the instrumentation side.
If you're a stupid computer, how do you know it's a vendor prefix?
Well, you can know from the provider name, okay?
Aaron Abbott (Google LLC) 00:51:02 Yeah, I think, I think also, I can't remember if I added it or not, but the… we said that the ones would not have… the OTAL ones won't have any dots.
So, I think you could… like, we could come up with a way to do it, but to your… to your kind of second point, like… Should we allow documenting?
vendor ones in the spec, or should we push people to try, for example, Anthropic, to try to Come up with a… non-vendor specific, because I think pretty much everybody has search result, so if we want them to normalize it, it would be nice for them to come and do it in the spec, or somebody to come and do it in the spec, right?
Liudmila Molkova 00:51:42 I mean, there could be ways. The only question for now I want to solve is… Do we provide any… stability guarantees for the any value. And, strictly speaking, from specification perspective.
We document that attribute values are not part of semantic convention stability guarantees.
So, we can maybe put an extra effort documenting this.
And… Yeah, that's probably the best thing we can do for now.
Aaron Abbott (Google LLC) 00:52:31 You mean the whole attribute?
Liudmila Molkova 00:52:33 Sorry.
Aaron Abbott (Google LLC) 00:52:35 You mean the whole attribute value, or just the specific part?
Liudmila Molkova 00:52:42 So the spec says that attribute value is not part of stability guarantees for semantic conventions. So, in theory, we could do a breaking change to the JSON schemas we have.
And it is not… formally, something, semantic convention would need a major version bump for. I don't think we should do it.
Aaron Abbott (Google LLC) 00:53:06 Yeah, yeah, I agree, okay.
Sorry, you want to go ahead, Trask?
Trask Stalnaker (Microsoft Corporation) 00:53:13 Yeah, would it even be breaking change to the JSON schema?
Liudmila Molkova 00:53:21 It would be a breaking change for the… the query, if somebody wrote a query for, let's say, anthropic.search result, and we made a search result a known, recognized, normalized part.
then all of a sudden, it would appear in a different place, and the query would break. Is it a drastic breaking that we should never, make?
Like, without major Russian bomb, maybe not.
Trask Stalnaker (Microsoft Corporation) 00:53:58 I see, so the… the… the braking would come if we… so everything would be, for now, as, prefix.
And then, if we wanted to normalize things at some point, across, providers, then we would do that, we would rename and that would… Yes, be some form of potentially breaking dashboards.
So we would need to consider Yeah, whether we want to hold those for major version bumps or not.
Liudmila Molkova 00:54:40 Yeah.
one thing I would propose is that I think the provider prefix should not be in the indication of being unknown.
like… It is… In the future, however we do it, I think it's totally fine to have provider-specific documented stable parts.
So maybe I… I would propose another prefix, like unknown, or… Something like this, that would say, we don't know what it is. Use it for your own risk.
Trask Stalnaker (Microsoft Corporation) 00:55:20 And the only reason we would do that is to avoid potential future conflicts if we wanted to use that same name. Trying to think, like, say, search results.
Why… why wouldn't we just use whatever the… Type.
That comes back.
Liudmila Molkova 00:55:44 I… I want to have some indication for the users that it's not…
Trask Stalnaker (Microsoft Corporation) 00:55:53 semantically defined.
Liudmila Molkova 00:55:55 Yes, and it can change, and that if we ever define the search result, Part. Done.
It's… It can have some schema expectations that whatever they have doesn't follow.
You can convince me to… just drop this idea of indication.
Trask Stalnaker (Microsoft Corporation) 00:56:34 I mean, it aligns with, like, so… Well, I guess what I… what we were… what it aligns in my head with, like, Java instrumentation that we would do, we would make this This would be an opt-in if it was not known, and… but we would use… I think we would still use the anthropic.the vendor prefix. We just would… Mark it as, like, an opt-in, since it's not part of these semantic conventions.
Liudmila Molkova 00:57:07 Would it concern you that Anthropic Dot would… Become part of semantic conventions at a later point.
Trask Stalnaker (Microsoft Corporation) 00:57:19 No, we would just then, capture it by default, not… it wouldn't be opt-in anymore.
Liudmila Molkova 00:57:27 So this is, like, the… the global experimental… Optin flag.
Mmm, I see. Okay, so then… stable.
Libraries don't capture unknown Parts by default.
But you can enable capturing.
Holo, holo.
And then… There is no indication on the part whether it's… Part of stability or not.
Trask Stalnaker (Microsoft Corporation) 00:58:04 That's essentially what we do in… Maybe not quite. We will… if it's instrumentation-specific, we'll… Yeah.
I don't know, and I'm not sure it completely fits here, but that was the first thing that lined up in my mind.
Liudmila Molkova 00:58:30 No, I think, yeah, yeah, I think it's a good idea, like, It's… there is some configuration that enables this, and this configuration is the contract.
Okay, I can…
Trask Stalnaker (Microsoft Corporation) 00:58:42 Let's see what else.
Liudmila Molkova 00:58:43 Go on from here.
Trask Stalnaker (Microsoft Corporation) 00:58:43 Yeah. Yeah.
Aaron Abbott (Google LLC) 00:58:45 Yeah, one quick concern with that is if… because these go inside of a list, we would then be, like, changing the indices of the list, for example. I think I think we have something for this in the spec for, like, invalid attributes. You're supposed to leave nulls behind when we do sanitization, for example, so… It's like a minor thing, but it's just kind of clunky, I think.
Liudmila Molkova 00:59:08 I didn't get it in what way?
Aaron Abbott (Google LLC) 00:59:10 like, so that people know that something was sanitized or removed, or opted out of.
Liudmila Molkova 00:59:19 Oh, they leave a placeholder instead?
Aaron Abbott (Google LLC) 00:59:22 I think… I think that's what we do for… Or at least used to do before complex attributes for span and metric attributes, if there were invalid values.
Liudmila Molkova 00:59:36 Let me think about it. Yeah.
I think, like, it's… we didn't replace the value, we just wrote the warning.
I think, and this is not a warning.
Trask Stalnaker (Microsoft Corporation) 01:00:03 I do think we also, like, we could make it work of capturing them all.
By default, and… and… Noting… some… How… Like, it doesn't… It doesn't… I want to say it doesn't bother me too much, But I do understand your point that it's almost like, yeah, like, these are experimental fields. Each one is kind of a field.
Almost a nested field.
Liudmila Molkova 01:00:40 Yeah.
Okay, let me play with different options, and we'll probably talk about this in the stabilization call, because this is where it should belong.
And, well, how do you.
Trask Stalnaker (Microsoft Corporation) 01:00:51 One minute.
Liudmila Molkova 01:00:51 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:00:52 Yes.
Liudmila Molkova 01:00:53 Somebody from Google really wants to come and present a trajectory ATV2 format for the community.
I'm curious what people think about it, how trajectories, if you heard the term, would be, aligned toward how it can work with OpenTelemetry together. Do we produce trajectories? Do we let providers transform telemetry into trajectories, and so on. If you are interested in the topic, please come next time, the December 1st meeting.
Trask Stalnaker (Microsoft Corporation) 01:01:30 Alright, I'm right on time.
Thank you all.
Liudmila Molkova 01:01:34 dear.
Jeff Leva 01:01:35 Thanks, everybody. Bye-bye.
Aaron Abbott (Google LLC) 01:01:36 later.
Trask Stalnaker (Microsoft Corporation) 01:01:37 I…
Pam Dixon 01:01:37 Thanks!
